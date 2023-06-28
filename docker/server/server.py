import json
import os

from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return 'Glory to Ukraine!'


@app.route('/hillel')
def hillel():
    data = {'Lesson': 'Docker',
                       'teacher': 'Vadym'}
    return json.dumps(data)


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
