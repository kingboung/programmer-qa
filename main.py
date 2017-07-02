#!/usr/bin/env python
# -*- coding:utf8 -*-

from flask import Flask, request, make_response, jsonify, Response
import json

app = Flask(__name__)


test = {
    'csdn': [
        {'question': 'xxx',
         'answer': [
             {
                 'author': 'xxx',
                 'time': 'xxx',
                 'content': 'xxx'
             },
             {
                 'author': 'xxx',
                 'time': 'xxx',
                 'content': 'xxx'
             },
             {
                 'author': 'xxx',
                 'time': 'xxx',
                 'content': 'xxx'
             }
         ]
         },
        {'question': 'xxx',
         'answer': [
             {
                 'author': 'xxx',
                 'time': 'xxx',
                 'content': 'xxx'
             },
             {
                 'author': 'xxx',
                 'time': 'xxx',
                 'content': 'xxx'
             },
             {
                 'author': 'xxx',
                 'time': 'xxx',
                 'content': 'xxx'
             }
         ]
         },
        {'question': 'xxx',
         'answer': [
             {
                 'author': 'xxx',
                 'time': 'xxx',
                 'content': 'xxx'
             },
             {
                 'author': 'xxx',
                 'time': 'xxx',
                 'content': 'xxx'
             },
             {
                 'author': 'xxx',
                 'time': 'xxx',
                 'content': 'xxx'
             }
         ]
         },
        {'question': 'xxx',
         'answer': [
             {
                 'author': 'xxx',
                 'time': 'xxx',
                 'content': 'xxx'
             },
             {
                 'author': 'xxx',
                 'time': 'xxx',
                 'content': 'xxx'
             },
             {
                 'author': 'xxx',
                 'time': 'xxx',
                 'content': 'xxx'
             }
         ]
         },
        {'question': 'xxx',
         'answer': [
             {
                 'author': 'xxx',
                 'time': 'xxx',
                 'content': 'xxx'
             },
             {
                 'author': 'xxx',
                 'time': 'xxx',
                 'content': 'xxx'
             },
             {
                 'author': 'xxx',
                 'time': 'xxx',
                 'content': 'xxx'
             }
         ]
         }
    ],
    'github': [
        {'question': 'xxx',
         'answer': [
             {
                 'author': 'xxx',
                 'time': 'xxx',
                 'content': 'xxx'
             },
             {
                 'author': 'xxx',
                 'time': 'xxx',
                 'content': 'xxx'
             },
             {
                 'author': 'xxx',
                 'time': 'xxx',
                 'content': 'xxx'
             }
         ]
         },
        {'question': 'xxx',
         'answer': [
             {
                 'author': 'xxx',
                 'time': 'xxx',
                 'content': 'xxx'
             },
             {
                 'author': 'xxx',
                 'time': 'xxx',
                 'content': 'xxx'
             },
             {
                 'author': 'xxx',
                 'time': 'xxx',
                 'content': 'xxx'
             }
         ]
         },
        {'question': 'xxx',
         'answer': [
             {
                 'author': 'xxx',
                 'time': 'xxx',
                 'content': 'xxx'
             },
             {
                 'author': 'xxx',
                 'time': 'xxx',
                 'content': 'xxx'
             },
             {
                 'author': 'xxx',
                 'time': 'xxx',
                 'content': 'xxx'
             }
         ]
         },
        {'question': 'xxx',
         'answer': [
             {
                 'author': 'xxx',
                 'time': 'xxx',
                 'content': 'xxx'
             },
             {
                 'author': 'xxx',
                 'time': 'xxx',
                 'content': 'xxx'
             },
             {
                 'author': 'xxx',
                 'time': 'xxx',
                 'content': 'xxx'
             }
         ]
         },
        {'question': 'xxx',
         'answer': [
             {
                 'author': 'xxx',
                 'time': 'xxx',
                 'content': 'xxx'
             },
             {
                 'author': 'xxx',
                 'time': 'xxx',
                 'content': 'xxx'
             },
             {
                 'author': 'xxx',
                 'time': 'xxx',
                 'content': 'xxx'
             }
         ]
         }
    ],
    'zhihu': [
        {'question': 'xxx',
         'answer': [
             {
                 'author': 'xxx',
                 'time': 'xxx',
                 'content': 'xxx'
             },
             {
                 'author': 'xxx',
                 'time': 'xxx',
                 'content': 'xxx'
             },
             {
                 'author': 'xxx',
                 'time': 'xxx',
                 'content': 'xxx'
             }
         ]
         }
    ],
    'stackoverflow': [
        {'question': 'xxx',
         'answer': [
             {
                 'author': 'xxx',
                 'time': 'xxx',
                 'content': 'xxx'
             },
             {
                 'author': 'xxx',
                 'time': 'xxx',
                 'content': 'xxx'
             },
             {
                 'author': 'xxx',
                 'time': 'xxx',
                 'content': 'xxx'
             }
         ]
         }
    ],
    'v2ex': [
        {'question': 'xxx',
         'answer': [
             {
                 'author': 'xxx',
                 'time': 'xxx',
                 'content': 'xxx'
             },
             {
                 'author': 'xxx',
                 'time': 'xxx',
                 'content': 'xxx'
             },
             {
                 'author': 'xxx',
                 'time': 'xxx',
                 'content': 'xxx'
             }
         ]
         }
    ]
}


"""首页"""
@app.route('/home', methods=['GET'])
def home():
    return "Hello Guangpan"


"""搜索"""
@app.route('/search', methods=['GET','POST'])
def search():

    question = request.form['question']
    print question

    """将问题传到爬虫"""


    """返回爬虫结果"""
    return Response(json.dumps(test), headers={'Access-Control-Allow-Origin' : '*'})


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)
