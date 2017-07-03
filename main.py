#!/usr/bin/env python
# -*- coding:utf8 -*-

from flask import Flask, request, make_response, jsonify, Response
from run_spider import run_spider
import json
import logging


#                       _oo0oo_
#                      o8888888o
#                      88" . "88
#                      (| -_- |)
#                      0\  =  /0
#                    ___/`---'\___
#                  .' \\|     |// '.
#                 / \\|||  :  |||// \
#                / _||||| -:- |||||- \
#               |   | \\\  -  /// |   |
#               | \_|  ''\---/''  |_/ |
#               \  .-\__  '-'  ___/-. /
#             ___'. .'  /--.--\  `. .'___
#          ."" '<  `.___\_<|>_/___.' >' "".
#         | | :  `- \`.;`\ _ /`;.`/ - ` : | |
#         \  \ `_.   \_ __\ /__ _/   .-` /  /
#     =====`-.____`.___ \_____/___.-`___.-'=====
#                       `=---='
#
#
#     ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#               佛祖保佑         永无BUG


app = Flask(__name__)


"""首页"""
@app.route('/home', methods=['GET'])
def home():
    return "Hello Guangpan"


"""搜索"""
@app.route('/search', methods=['POST'])
def search():
    question = request.form['question']

    logging.info("Get the search: %s" % search)


    """将问题传到爬虫并返回爬虫结果"""
    csdn_cursor = run_spider('CSDN_spider', search=search)
    stackoverflow_cursor = run_spider('Stackoverflow_spider', search=search)


    """返回爬虫结果"""
    result = {}


    # CSDN结果
    result['csdn'] = []
    index = 0

    for doc in csdn_cursor:
        result['csdn'].append({})
        result['csdn'][index]['question'] = doc['topic']
        result['csdn'][index]['answer'] = doc['answer']
        index += 1


    # Stackoverflow结果
    result['stackoverflow'] = []
    index = 0

    for doc in stackoverflow_cursor:
        result['stackoverflow'].append({})
        result['stackoverflow'][index]['question'] = doc['topic']
        result['stackoverflow'][index]['description'] = doc['question']
        result['stackoverflow'][index]['answer'] = doc['answers']

    return Response(json.dumps(result), headers={'Access-Control-Allow-Origin': '*'})


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)
