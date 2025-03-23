from flask import Flask, render_template, request
from markupsafe import escape
from vsearch import search4letters
from pathlib import Path
import mariadb

app = Flask(__name__)

log_dir = Path('var')
log_name = Path('vsearch.log')
log_file = log_dir / log_name


def log_request(req: 'flask_request', res: str) -> None:
    """Log details of the web request and the results."""
    # Lo anterior:
    # with open(log_file, 'a') as log:
    #     print(req.form, req.remote_addr, req.user_agent, res, file=log, sep='|')

    # Solo req.user_agent.string tiene contenido.
    # print(dir(req))
    # print(dir(req.user_agent))
    # print(f'{req.user_agent.browser=}', f'{req.user_agent.language=}', f'{req.user_agent.platform=}',
    #       f'{req.user_agent.string=}', f'{req.user_agent.to_header=}', f'{req.user_agent.version=}')

    dbconfig = {'host': '127.0.0.1',
                'user': 'vsearch',
                'password': 'vsearchpasswd',
                'database': 'vsearchlogDB', }
    conn = mariadb.connect(**dbconfig)
    cursor = conn.cursor()
    _SQL = """insert into log  
              (phrase, letters, ip, browser_string, results) 
              values 
              (%s, %s, %s, %s, %s)"""
    cursor.execute(_SQL, (req.form['phrase'],
                          req.form['letters'],
                          req.remote_addr,
                          req.user_agent.string,
                          res, ))
    conn.commit()
    cursor.close()
    conn.close()


@app.route('/search4', methods=['POST'])
def do_search() -> 'html':
    phrase = request.form['phrase']
    letters = request.form['letters']
    results = str(search4letters(phrase, letters))
    title = 'Here are your results'
    log_request(request, results)
    return render_template('results.html', the_title=title, the_phrase=phrase,
                           the_letters=letters, the_results=results)


@app.route('/')
@app.route('/entry')
def entry_page() -> 'html':
    return render_template('entry.html', the_title='Welcome to the search4letters on the web!')


@app.route('/viewlog')
def view_the_log() -> str:
    content = []
    with open(log_file) as log:
        for line in log:
            content.append([])
            for item in line.split('|'):
                content[-1].append(escape(item))

    title = 'Log View'
    row_titles = ('Form Data', 'Remote_addr', 'User_agent', 'Results')
    return render_template('viewlog.html', the_title=title, the_row_titles=row_titles, the_data=content)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
