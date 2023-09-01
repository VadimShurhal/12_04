import json
import logging
import os

from flask import Flask, request

app = Flask(__name__)

logging.basicConfig(filename='record.log', level=logging.DEBUG, format=f'%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')

PARAMS = []


@app.get("/")
def home():
    text = 'Glory to Ukraine!'
    app.logger.info(f'Main page with content {text}')
    return text


@app.get('/hillel')
def hillel():
    data = {'Lesson': 'Docker',
            'teacher': 'Vadym'}
    app.logger.info(f'Main page with data {data}')
    return json.dumps(data)


@app.post('/search')
def search():
    # args = request.args.to_dict()
    args = {'name': "John",
            'age': 11}
    PARAMS.append(args)
    app.logger.info(f'Params {args} successfully added in parameters list ')
    return json.dumps(PARAMS)


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
