from app import app
from flask import render_template

@app.route("/")
def main():
    return render_template('index.html')

@app.route("/hello")
def hello():
    return "hello world!"

@app.route('/template/')
@app.route('/template/<name>')
def hello2(name=None):
    return render_template('hello.html', name=name)
