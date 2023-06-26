import json

from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Glory to Ukraine!"


@app.route('/hillel')
def index():
    return json.dumps({'Lesson': 'Docker',
                       'teacher': 'Vadym'})


if __name__ == '__main__':
    app.run(debug=True)
