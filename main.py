#!/usr/bin/env python
# -*- coding:utf8 -*-

from flask import Flask, request, make_response, jsonify, Response
import json
import pymongo


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
@app.route('/search', methods=['GET', 'POST'])
def search():
    question = request.form['question']


    print question

    """将问题传到爬虫"""

    """返回爬虫结果"""
    client = pymongo.MongoClient(host="localhost", port=27017)
    db = client.get_database("programmerQA")
    collection = db.get_collection('csdn')

    cursor = collection.find({"search": "404 not found"})

    result = {}
    result['csdn'] = []

    index = 0

    for doc in cursor:
        result['csdn'].append({})
        result['csdn'][index]['question'] = doc['topic']
        result['csdn'][index]['answer'] = doc['answer']
        index += 1

    print result

    return Response(json.dumps(result), headers={'Access-Control-Allow-Origin': '*'})


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)
