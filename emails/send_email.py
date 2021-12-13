import requests
from bs4 import BeautifulSoup
import time
import hmac
import hashlib
import base64
import urllib.parse
import json

"""
#!api-excel/send_email 
# -*- coding:utf-8 -*-
# Author:周倩
# name:发送报警信息到钉钉群提醒测试人员
"""


def send_email():
    timestamp = str(round(time.time() * 1000))
    secret = 'SECfa946cbe63194261862498aacaa52882f32906aee0671bdfc9052f2e6da5f518'  # 这里填的就是上面获取的加签密钥
    secret_enc = secret.encode('utf-8')
    string_to_sign = '{}\n{}'.format(timestamp, secret)
    string_to_sign_enc = string_to_sign.encode('utf-8')
    hmac_code = hmac.new(secret_enc, string_to_sign_enc, digestmod=hashlib.sha256).digest()
    sign = urllib.parse.quote_plus(base64.b64encode(hmac_code))

    # 把第二步中获取到的 timestamp和sign拼接到URL中
    url = 'https://oapi.dingtalk.com/robot/send?access_token=7891bb310cdda1c68b0649fa7e87589d62cf6c3741d949c579f7c7fe1acd26ca' + '&timestamp=' + timestamp + '&sign=' + sign
    h = {'content-type': 'application/json',
         'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:22.0) Gecko/20100101 Firefox/22.0'}
    # d里面的at参数是需要at的人参数，只有at的人存在这个参数里面才会@成功
    d = json.dumps({"msgtype": "text", "text": {"content": '接口自动化测试未全部通过'}})
    req = requests.post(url, data=d, headers=h)
