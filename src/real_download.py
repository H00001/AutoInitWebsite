# -*- coding:utf-8 -*-

import time

import requests

from src.LikList import lknks
from src.dd.realdown.util import titleinsp


def doDownTouTiao(article_info, bp):
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:46.0) Gecko/20100101 Firefox/46.0',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Connection': 'Keep-Alive',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
    }
    article_html = requests.get("https://www.toutiao.com/a" + article_info[0].split("/")[4], headers=headers)
    article_html.encoding = 'utf-8'
    unixtime = str(time.time())

    text = titleinsp.maintextinsp(article_html.text)
    try:
        stainfojson = text.index("articleInfo")
        endinfojson = text.index("groupId", stainfojson + 10)
    except Exception:
        print(article_info[0]+" is error")
        return
    text = text[stainfojson + 15:endinfojson - 3]
    text = '''<!DOCTYPE html><html><head><meta charset="utf-8"></head><body>''' + text + '''</body></html>'''

    lknks.append([unixtime, article_info[1]])
    file_object = open(bp + 'fil_n/' + unixtime + '.html', 'w+', encoding='utf-8')
    file_object.write(text)
    file_object.close()

def mkdir(path):
    import os
    path = path.strip()
    path = path.rstrip("\\")
    isExists = os.path.exists(path)
    if not isExists:

        os.makedirs(path)
        return True
    else:
        return False


