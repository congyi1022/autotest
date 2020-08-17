# coding:utf-8
import requests
from bs4 import BeautifulSoup
import logging
from utils import getTokenAndCookie


class sendRequest:
    def sendRequest(self,url,email,pw):
        datas = getTokenAndCookie.getToken(url)
        session = requests.session()
        session.cookies=datas["cookie"]
        crsf_token=datas["token"]
        postData = {
                "csrf_token": crsf_token,
                "email": email, "password": pw}
        res=session.post(url,data=postData)
        return res


