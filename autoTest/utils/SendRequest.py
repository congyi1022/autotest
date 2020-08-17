# coding:utf-8
import requests
from bs4 import BeautifulSoup
import logging
from utils import getTokenAndCookie
from requests.cookies import RequestsCookieJar


class SendRequest:
    def sendRequest(self, url, email, pw):
        datas = getTokenAndCookie.getToken(url)
        crsf_token = datas["token"]
        postData = {
            "csrf_token": crsf_token,
            "email": email, "password": pw}
        res = requests.post(url, data=postData, cookies=datas["cookie"])
        return res
