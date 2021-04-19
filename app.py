from flask import Flask

app = Flask(__name__)

template = 'temp.html'


@app.route('/main')
def home():
    return template


if __name__ == '__main__':
    app.run()
