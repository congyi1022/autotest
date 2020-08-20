# coding:utf-8
import requests
from bs4 import BeautifulSoup
import logging
from utils import getTokenAndCookie
from utils import readExcel
import json
from requests.cookies import RequestsCookieJar


class RunMain:

    def sendRequest(self, url, postData):

        datas = getTokenAndCookie.getToken(url)
        crsf_token = datas["token"]
        post_data = json.loads(postData)
        post_data["csrf_token"] = crsf_token
        res = requests.post(url, data=post_data, cookies=datas["cookie"])
        return res

    def sendGetRequest(self, url, data=None):
        res = requests.get(url, data)
        return res

    def sendPostRequest(self, url, data, cookie=None):
        res = requests.post(url, data, cookie)
        return res

    def main_request(self, method, url, data=None, cookie=None):
        res = None
        if method == "GET":
            self.sendGetRequest(url, data)
        elif method == "POST":
            self.sendPostRequest(url, data, cookie)
        return res
