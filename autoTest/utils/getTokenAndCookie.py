# coding:utf-8

import requests
from bs4 import BeautifulSoup


def getToken(url):
    datas = {}
    res = requests.get(url)
    # 将RequestsCookieJar转换成字典
    # cookie = requests.utils.dict_from_cookiejar(res.cookies)
    cookie = res.cookies
    datas["cookie"] = cookie
    soup = BeautifulSoup(res.text, "html.parser")
    find_all = soup.find_all("input", attrs={"id": "csrf_token", "name": "csrf_token", "type": "hidden"})
    token = find_all[0].attrs["value"]
    datas["token"] = token

    return datas
