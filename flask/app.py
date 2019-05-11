# -*- coding: utf-8 -*-
from time import gmtime, strftime
from flask import Flask, request, Response
from flask.logging import default_handler
import logging
import json

# from * import * as api_func


class RequestFormatter(logging.Formatter):
    def format(self, record):
        record.url = request.url
        record.remote_addr = request.remote_addr
        return super().format(record)


formatter = RequestFormatter(
    '[%(asctime)s] %(remote_addr)s requested %(url)s\n'
    '%(levelname)s in %(module)s: %(message)s'
)
default_handler.setFormatter(formatter)
app = Flask(__name__)


@app.route('/', methods=['POST', 'OPTIONS'])
def main():
    if request.method == 'OPTIONS':
        res = Response('')
        res.headers['Access-Control-Allow-Origin'] = 'null'
        res.headers['Access-Control-Allow-Methods'] = 'POST,OPTIONS'
        return res

    if request.method == 'POST':
        try:
            print(strftime("%Y-%m-%d %H:%M:%S", gmtime()))

            body = request.get_json(silent=True)
            data = body.get("data")

            #
            result = [api_func(d) for d in data]

            ret = json.dumps({'code': 1, 'data': result})
            return ret
        except Exception as e:
            print(e)
            return json.dumps({'code': 0, 'data': 'unknown error'})


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
