import requests
import re
from lxml import etree
import json

def parse_url(**kwargs):
    re_data=json.loads(kwargs['requests_data'])
    print(re_data)
    try:
        if kwargs['requests_method'] == 'post':
            resp = requests.post(
                kwargs['requests_url'], data=re_data, headers=kwargs['requests_headers'])
        else:
            resp = requests.get(kwargs['requests_url'],params=re_data)

        if resp.status_code == 200:
            # 处理一下网站打印出来中文乱码的问题
            resp.encoding = kwargs['requests_charset']
            return resp
        return None
    except ConnectionError:
        print("Error.")
    return None


def book_search(sources_data, **kwargs):
    search_data=parse_url(**kwargs)
    if search_data:
        html = etree.HTML(search_data.text)
        search_key = [k for k in sources_data.keys()]
        search_value = (html.xpath(v) for v in sources_data.values())
        search_values = [dict(zip(search_key, vv)) for vv in zip(*search_value)]
        print(search_values)
    else:
        print('搜索失败')


def abc1(book_data):
    search_key=book_data['search_key'].split(",")
    search_value=book_data['search_value'].split(",")

    search_data=parse_url(**book_data)
    if search_data:
        html = etree.HTML(search_data.text)
        search_value=[html.xpath(v) for v in search_value]
        search_values = [dict(zip(search_key, vv)) for vv in zip(*search_value)]
        print(search_values)
    else:
        print('搜索失败')


if __name__ == '__main__':
    pass
    _sources_data = {
        'bookName': '//*[@id="nr"]/td[1]/a/text()',
        'bookAuthor': '//*[@id="nr"]/td[3]/text()',
        'bookNewestChapterName': '//*[@id="nr"]/td[2]/a/text()',
        'bookUpdateTime': '//*[@id="nr"]/td[5]/text()',
        'bookUrl': '//*[@id="nr"]/td[1]/a/@href'
    }
    _search_key="bookName,bookAuthor,bookNewestChapterName,bookUpdateTime,bookUrl".split(",")
    _sources_data='//*[@id="nr"]/td[1]/a/text(),//*[@id="nr"]/td[3]/text(),//*[@id="nr"]/td[2]/a/text(),//*[@id="nr"]/td[5]/text(),//*[@id="nr"]/td[1]/a/@href'.split(",")

    # _sources_data=['//*[@id="nr"]/td[1]/a/text()','//*[@id="nr"]/td[3]/text()','//*[@id="nr"]/td[2]/a/text()','//*[@id="nr"]/td[5]/text()','//*[@id="nr"]/td[1]/a/@href']
    abc1(_search_key,_sources_data, url='https://www.i7wx.com/modules/article/search.php?searchkey=%BD%A3%C0%B4&searchtype=articlename',method='get', data='', charset='gbk')
    # book_search(_sources_data, url='https://www.i7wx.com/modules/article/search.php?searchkey=%BD%A3%C0%B4&searchtype=articlename',
    #             method='get', data='', charset='gbk')
    # book_search(url='http://www.88xiaoshuo.com/modules/article/search.php?searchkey=%BD%A3%C0%B4&searchtype=articlename',method='get',data='',charset='gbk')
    