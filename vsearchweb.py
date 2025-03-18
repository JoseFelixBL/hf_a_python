from flask import Flask, render_template, request
from markupsafe import escape
from vsearch import search4letters
from pathlib import Path

app = Flask(__name__)

log_dir = Path('var')
log_name = Path('vsearch.log')
log_file = log_dir / log_name


def log_request(req: 'flask_request', res: str) -> None:
    with open(log_file, 'a') as log:
        print(req.form, req.remote_addr, req.user_agent, res, file=log, sep='|')


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
    with open(log_file) as log:
        contents = log.read()
    return escape(contents)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
