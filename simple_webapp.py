from flask import Flask, session

app = Flask(__name__)
app.secretkey = 'YouWillNeverGuessMySecretKey'


@app.route('/')
def hello() -> str:
    return 'Hello from the simple webapp.'


@app.route('/page1')
def page1() -> str:
    return 'This is page 1.'


@app.route('/page2')
def page2() -> str:
    return 'This is page 2.'


@app.route('/page3')
def page3() -> str:
    return 'This is page 3.'


@app.route('/login')
def login() -> 'str':
    session['logged_in'] = True
    return 'You are now logged in'


@app.route('/logout')
def login() -> 'str':
    session['logged_in'].clear()
    return 'You are now logged OUT'


if __name__ == '__main__':
    app.run(debug=True)
