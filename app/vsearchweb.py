from flask import Flask, render_template, request, session
from flask import copy_current_request_context
from markupsafe import escape
from threading import Thread
import os

from vsearch import search4letters
from DBcm import UseDatabase, DBConnectionError, CredentialsError, SQLError
from checker import check_logged_in

from time import sleep

app = Flask(__name__)
app.secret_key = 'YouWillNeverGuessMySecretKey'

HOST = os.getenv('DB_HOST')
if HOST is None or HOST == '':
    HOST = '127.0.0.1'

app.config['dbconfig'] = {'host': HOST,
                          'user': 'vsearch',
                          'password': 'vsearchpasswd',
                          'database': 'vsearchlogDB', }


@app.route('/search4', methods=['POST'])
def do_search() -> 'html':

    @copy_current_request_context
    def log_request(req: 'flask_request', res: str) -> None:
        """Log details of the web request and the results."""
        sleep(15)  # This makes log_request very slow...
        with UseDatabase(app.config['dbconfig']) as cursor:
            _SQL = """insert into log  
                    (phrase, letters, ip, browser_string, results) 
                    values 
                    (%s, %s, %s, %s, %s)"""
            cursor.execute(_SQL, (req.form['phrase'],
                                  req.form['letters'],
                                  req.remote_addr,
                                  req.user_agent.string,
                                  res, ))

    phrase = request.form['phrase']
    letters = request.form['letters']
    results = str(search4letters(phrase, letters))
    title = 'Here are your results'
    try:
        # log_request(request, results)
        t = Thread(target=log_request, args=(request, results))
        t.start()
    except Exception as err:
        print('***** Logging failed with error:', str(err))
    return render_template('results.html',
                           the_title=title,
                           the_phrase=phrase,
                           the_letters=letters,
                           the_results=results)


@app.route('/')
@app.route('/entry')
def entry_page() -> 'html':
    return render_template('entry.html', the_title='Welcome to the search4letters on the web!')


@app.route('/viewlog')
@check_logged_in
def view_the_log() -> 'html':
    try:
        with UseDatabase(app.config['dbconfig']) as cursor:
            _SQL = """select ts, phrase, letters, ip, browser_string, results
                    from log"""
            cursor.execute(_SQL)
            content = cursor.fetchall()
        title = 'Log View'
        row_titles = ('Time Stamp', 'Phrase', 'Letters',
                      'Remote_addr', 'User_agent', 'Results')
        return render_template('viewlog.html', the_title=title, the_row_titles=row_titles, the_data=content)
    except DBConnectionError as err:
        print('Is your database switched on? Error:', str(err))
    except CredentialsError as err:
        print('User-id/Password issues. Error:', str(err))
    except SQLError as err:
        print('Is your query correct? Error:', str(err))
    except Exception as err:
        print('Something went wrong:', str(err))
    return 'error'


@app.route('/login')
def login() -> 'str':
    session['logged_in'] = True
    return 'You are now logged in'


@app.route('/logout')
def logout() -> 'str':
    if 'logged_in' in session:
        session.pop('logged_in')
    return 'You are now logged OUT'


@app.route('/log_status')
def log_status() -> 'str':
    if 'logged_in' in session:
        return 'You are logged in'
    return 'You are NOT logged in'


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
