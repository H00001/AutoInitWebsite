import requests
import json


def getArticleInfoFromTouTiao(keyword, offset):
    requesturl = requests.get(
        "https://www.toutiao.com/search_content/?offset=" + str(offset) + "&format=json&keyword=" + keyword + "&autoload=true&count=20&cur_tab=1")
    loads = json.loads(requesturl.text)
    article_list = []
    for i in range(20):
        try:
            article_list.append([loads["data"][i]["article_url"], loads["data"][i]["title"]])
        except Exception as e:
            pass
    return article_list
