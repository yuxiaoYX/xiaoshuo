import requests
import re
from lxml import etree
import json
import json5
from urllib.parse import quote

# def parse_url(kwargs):
#     # re_data=json.loads(kwargs['requests_data'])
#     # re_data['searchkey']=searchkey.encode(kwargs['requests_charset'])
#     try:
#         if kwargs['requests_method'] == 'post':
#             resp = requests.post(
#                 kwargs['requests_url'], data=kwargs['requests_data'], headers=kwargs['requests_headers'])
#         else:
#             resp = requests.get(
#                 kwargs['requests_url'], params=kwargs['requests_data'])
#         if resp.status_code == 200:
#             # 处理一下网站打印出来中文乱码的问题
#             resp.encoding = kwargs['requests_charset']
#             return resp
#         return None
#     except ConnectionError:
#         print("Error.")
#     return None


def parse_url(url, encoding):
    try:
        resp = requests.get(url)
        if resp.status_code == 200:
            # 处理一下网站打印出来中文乱码的问题
            resp.encoding = encoding
            return resp
        return None
    except ConnectionError:
        print("Error.")
    return None


def SourceJson(source):
    with open("源正则.json", 'r', encoding='utf-8') as load_f:
        load_dict = json5.load(load_f)
        # print(load_dict)
    return load_dict[source]

# def book_search(searchkey, book_data):
#     re_data = json.loads(book_data['requests_data'])
#     re_data['searchkey'] = searchkey.encode(book_data['requests_charset'])
#     book_data['requests_data'] = re_data
#     search_data = parse_url(book_data)
#     if search_data:
#         search_key = book_data['search_key'].split(",")
#         search_value = book_data['search_value'].split(",")

#         html = etree.HTML(search_data.text)
#         search_value = [html.xpath(v) for v in search_value]
#         search_values = [dict(zip(search_key, vv))
#                          for vv in zip(*search_value)]
#         return search_values
#     else:
#         return {'state': '搜索失败'}


def book_search(searchKeyword, source):
    source_json = SourceJson(source)
    search_Url = source_json["search"]['searchUrl'] % quote(searchKeyword.encode(source_json['Encoding']))
    search_data = parse_url(search_Url, source_json['Encoding'])
    source_json = source_json["search"]
    if search_data:
        search_key = source_json['searchKey'].split(",")
        search_value = source_json['searchValue'].split(",")
        html = etree.HTML(search_data.text)
        books = html.xpath(source_json['books'])[0]
        search_value = [books.xpath(v) for v in search_value]
        search_values = [dict(zip(search_key, vv))for vv in zip(*search_value)]
        return search_values
    else:
        return {'state': '搜索失败'}


# def book_jieshao(book_data):
#     jieshao_data = parse_url(book_data)
#     if jieshao_data:
#         jieshao_key = book_data['introduce_key'].split(",")
#         jieshao_value = book_data['introduce_value'].split(",")

#         html = etree.HTML(jieshao_data.text)
#         jieshao_value = [html.xpath(v) for v in jieshao_value]
#         jieshao_value[2] = [''.join(jieshao_value[2])]  # 取多行简介
#         jieshao_values = [dict(zip(jieshao_key, vv))for vv in zip(*jieshao_value)]
#         return jieshao_values
#     else:
#         return {'state': '搜索失败'}
def book_jieshao(detailUrl, source):
    source_json = SourceJson(source)
    jieshao_data = parse_url(detailUrl, source_json['Encoding'])
    if jieshao_data:
        html = etree.HTML(jieshao_data.text)
        jieshao_books = html.xpath(source_json['detailBooks'])[0]
        jieshao_values = {}
        for k, v in source_json['details'].items():
            jieshao_values[k] = ''.join(jieshao_books.xpath(v))
        return jieshao_values
    else:
        return {'state': '搜索失败'}


def book_list(chapterLink, source):
    source_json = SourceJson(source)
    list_data = parse_url(
        source_json['host']+chapterLink, source_json['Encoding'])
    pattern = re.compile(source_json['chapters']['chapterList'])
    result = pattern.findall(list_data.text)
    return result


def book_content(contentUrl, source):
    source_json = SourceJson(source)
    content_data = parse_url(source_json['host']+contentUrl, source_json['Encoding'])
    pattern = re.compile(source_json['contents']['content_KV'])
    result = pattern.findall(content_data.text)[0]
    if result:
        for k, v in source_json['contents']['contentReplace'].items():  # 替换内容
            result = result.replace(k, v)
        result = result.split('<br/>')  # 字符串转列表
        return result
    else:
        return {'state': '获取内容失败'}


if __name__ == '__main__':
    # book_list()
    # book_content()
    pass
    # print(book_search("剑来","爱奇文学"))
    print(book_jieshao('https://www.i7wx.com/book/35344.html',"爱奇文学"))
    # print(book_list("https://www.i7wx.com/book/16/16012/"))
    # print(book_content("https://www.i7wx.com/book/16/16012/33475.html", "爱奇文学"))
