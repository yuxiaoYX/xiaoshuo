import requests
import re
from lxml import etree

def parse_url(**kw):
    try:
        if kw['method'] == 'post':
            resp = requests.post(kw['url'], data=kw['data'],headers=kw['headers'])
        else:
            resp = requests.get(kw['url'])

        if resp.status_code == 200:
            # 处理一下网站打印出来中文乱码的问题
            resp.encoding = kw['charset']
            return resp
        return None
    except ConnectionError:
        print("Error.")
    return None


def book_search(**kw):
    print(kw)

    search_data = parse_url(**kw)
    # print(search_data.text)
    html = etree.HTML(search_data.text)
    html_data=html.xpath('//*[@id="conn"]/table/tbody')
    print(html_data)
    print(html.tostring(html_data[0]))
    # aa=html_data.xpath('@td')
    # print(aa)

if __name__ == '__main__':
    pass
    book_search(url='https://www.i7wx.com/modules/article/search.php?searchkey=%BD%A3%C0%B4&searchtype=articlename',method='get',data='',charset='gbk')
