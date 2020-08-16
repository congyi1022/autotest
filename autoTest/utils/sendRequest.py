# coding:utf-8
import requests
from bs4 import BeautifulSoup
import logging


class sendRequest:

    def __init__(self):
        self.cookie = None

    def getCsrfToken(self):
        url="http://127.0.0.1:5000/login"
        sessions = requests.session()
        res= sessions.get(url)
        self.cookie = res.cookies
        # print(self.cookie)
        logging.info("cookie",res.cookies)

        soup = BeautifulSoup(res.text, "html.parser")
        find_all = soup.find_all("input", attrs={"id": "csrf_token", "name": "csrf_token", "type": "hidden"})
        token = find_all[0].attrs["value"]
        return token

    def sendrequest(self,email,pw):
        url = "http://127.0.0.1:5000/login"
        token = self.getCsrfToken()
        sessions = requests.session()
        sessions.cookies = self.cookie
        datas = {
            "csrf_token": token,
            "email": email, "password": pw}
        r = sessions.post(url, data=datas)
        return r

