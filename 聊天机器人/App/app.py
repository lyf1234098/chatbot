import json
import re

import requests
from flask import Flask,Blueprint, render_template, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

REQUEST_URL = "http://localhost:5005/webhooks/rest/webhook"
HEADERS = {'Content-Type': 'application/json; charset=utf-8'}

@app.route('/', methods=['GET', 'POST'])
def test():
    # return 'this a test page', 200
    return render_template('chat.html')

@app.route('/chat',methods=['GET'])
def chat():
    data=request.args.to_dict()
    message=data['message']
    if message:
        answer = rasaresponse('zhongshan',message)
        return answer



def rasaresponse(user,msg):
    requestDict={'sender':user,'message':msg}
    rsp=requests.post(REQUEST_URL, data=json.dumps(requestDict),headers=HEADERS)
    print(rsp.text)
    # content=rsp.text.encode('utf-8').decode("unicode-escape")
    if rsp.status_code == 200:
        rsp_json=json.loads(rsp.text.encode())

        content_text = ''
        if len(rsp_json):
            # print(rsp_json)
            for i in range(len(rsp_json)):
                # txt_=rsp_json[i]['text']
                txt_=rsp_json[i].get('text')
                print('rasa返回内容是---------->{}'.format(txt_))
                if txt_:
                    content_text=content_text+txt_
                else:
                    content_text=content_text + '\n' + rsp_json[i]['image']
          
            return content_text

        else:
            return '哎呀,这个小美也不懂呢～～～'

    else:
        return '返回错误，请重新输入问话。'

if __name__ == '__main__':
        app.debug = True
        app.run(host='0.0.0.0', port=5000)
