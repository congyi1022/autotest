# coding:utf-8
import requests
from bs4 import BeautifulSoup
import logging
from utils import getTokenAndCookie
from utils import readExcel
import json
from requests.cookies import RequestsCookieJar


class SendRequest:

       def sendRequest(self, url, postData):
        datas = getTokenAndCookie.getToken(url)
        crsf_token = datas["token"]
        post_data = json.loads(postData)
        post_data["csrf_token"] = crsf_token
        res = requests.post(url, data=post_data, cookies=datas["cookie"])
        return res
