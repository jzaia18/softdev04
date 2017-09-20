# Jake Zaia
# SoftDev pd 9
# Work 04
# 2017-09-20

from flask import Flask

app = Flask(__name__)


@app.route('/')
def main():
    return 'welcome to main!'

@app.route('/dog')
def dog():
    return 'welcome to dog!'

@app.route('/cat')
def cat():
    return 'welcome to cat!'


if __name__ == '__main__':
    app.run()
