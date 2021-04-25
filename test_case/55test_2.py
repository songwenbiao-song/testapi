
#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author tom
import requests
import json

def dingTalk1():
    headers={
        "Content-Type": "application/json"
    }
    data={"msgtype": "text",
          "text": {
              "content": "我就是我, 是不一样的烟火"
          }
          }
    json_data=json.dumps(data)
    p=requests.post(url='https://oapi.dingtalk.com/robot/send?access_token=2e120cee5a317bbec476c5d1e2e977355539b396944e24085ce026bdf27e196b',data=json_data,headers=headers)
    print(p.json())


p = dingTalk1()
print(p)



import requests
import json

def dingTalk():
    headers={
        "Content-Type": "application/json"
    }
    data={"msgtype": "text",
          "text": {
              "content": "我就是我, 是不一样的烟火"
          }
          }
    json_data=json.dumps(data)
    p=requests.post(url='https://oapi.dingtalk.com/robot/send?access_token=2e120cee5a317bbec476c5d1e2e977355539b396944e24085ce026bdf27e196b',data=json_data,headers=headers)
    print(p.json())

p=dingTalk()
print(p)