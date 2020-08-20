# coding:utf-8
import requests


class RunMain:

    def sendGetRequest(self, url, data=None):
        res = requests.get(url, data)
        return res

    def sendPostRequest(self, url, post_data, cookie):
        res = requests.post(url, data=post_data, cookies=cookie)
        return res

    def main_request(self, method, url, data=None, cookie=None):
        res = None
        if method == "GET":
            res = self.sendGetRequest(url, data)
        elif method == "POST":
            res = self.sendPostRequest(url, data, cookie)
        return res
