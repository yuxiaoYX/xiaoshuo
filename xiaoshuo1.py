import requests
import re
from lxml import etree
import json


def parse_url(kwargs):
    # re_data=json.loads(kwargs['requests_data'])
    # re_data['searchkey']=searchkey.encode(kwargs['requests_charset'])
    try:
        if kwargs['requests_method'] == 'post':
            resp = requests.post(
                kwargs['requests_url'], data=kwargs['requests_data'], headers=kwargs['requests_headers'])
        else:
            resp = requests.get(
                kwargs['requests_url'], params=kwargs['requests_data'])
        if resp.status_code == 200:
            # 处理一下网站打印出来中文乱码的问题
            resp.encoding = kwargs['requests_charset']
            return resp
        return None
    except ConnectionError:
        print("Error.")
    return None


def book_search(searchkey, book_data):
    re_data = json.loads(book_data['requests_data'])
    re_data['searchkey'] = searchkey.encode(book_data['requests_charset'])
    book_data['requests_data'] = re_data
    search_data = parse_url(book_data)
    if search_data:
        search_key = book_data['search_key'].split(",")
        search_value = book_data['search_value'].split(",")

        html = etree.HTML(search_data.text)
        search_value = [html.xpath(v) for v in search_value]
        search_values = [dict(zip(search_key, vv))
                         for vv in zip(*search_value)]
        return search_values
    else:
        return {'state': '搜索失败'}


def book_jieshao(book_data):
    jieshao_data = parse_url(book_data)
    if jieshao_data:
        jieshao_key = book_data['introduce_key'].split(",")
        jieshao_value = book_data['introduce_value'].split(",")

        html = etree.HTML(jieshao_data.text)
        jieshao_value = [html.xpath(v) for v in jieshao_value]
        jieshao_value[2] = [''.join(jieshao_value[2])]  # 取多行简介
        jieshao_values = [dict(zip(jieshao_key, vv))for vv in zip(*jieshao_value)]
        return jieshao_values
    else:
        return {'state': '搜索失败'}


if __name__ == '__main__':
    pass
