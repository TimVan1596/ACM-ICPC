from flask import Flask, url_for, render_template
from markupsafe import escape

app = Flask(__name__)


@app.route('/')
def index():
    return '<h1>Hello World</h1>' \
           '<div><a href="/hello/" target="_blank">跳转test</a></div>'


@app.route("/test/<name>")
def test(name):
    return f"<h1>Hello, {escape(name)}!</h1>"


@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)


# with app.test_request_context():
#     print(url_for('index'))
#     print(url_for('index', next='/'))
#     print(url_for('test', name='John Doe'))

if __name__ == '__main__':
    app.run('127.0.0.1', 5000)
