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
    sources_data={
        'bookName':'//*[@id="nr"]/td[1]/a/text()',
        'bookAuthor':'//*[@id="nr"]/td[3]/text()',
        'bookNewestChapterName':'//*[@id="nr"]/td[5]/text()',
        'bookUpdateTime':'//*[@id="nr"]/td[2]/a/text()',
        'bookUrl':'//*[@id="nr"]/td[1]/a/@href'
    }

    print(kw)
    search_data = parse_url(**kw)
    # print(search_data.text)
    html = etree.HTML(search_data.text)
    # b='//*[@id="nr"]/td/a/text() | //*[@id="nr"]/td/a/@href | //*[@id="nr"]/td/text()'
    c = ['book_name','book_author','book_newest_hapter_ame','book_update_time','book_url']
    for k,v in sources_data.items():
        cc=html.xpath(v)
        print({k:cc})
    

    # c=['bookName','bookAuthor','bookNewestChapterName','bookUpdateTime','bookUrl']
    # cc=['https://www.i7wx.com/book/35344.html', '剑来', ' 第653章 可惜下雨不下钱（二）', '烽火戏诸侯', '19-05-21', 'https://www.i7wx.com/book/75523.html', '剑来', ' 第九章：痴……女？', '老油条本尊',  '19-01-21',  'https://www.i7wx.com/book/4473.html', '剑来',  ' 第四十五章 白马下青山', '暮鼓晨钟', '18-03-03']
    # ccc=(cc[i:i+5] for i in range(0,len(cc),5))
    # cccc=[dict(zip(c,ii)) for ii in ccc]
    # print(cccc)

if __name__ == '__main__':
    pass
    # book_search(url='https://www.i7wx.com/modules/article/search.php?searchkey=%BD%A3%C0%B4&searchtype=articlename',method='get',data='',charset='gbk')
    # book_search(url='http://www.88xiaoshuo.com/modules/article/search.php?searchkey=%BD%A3%C0%B4&searchtype=articlename',method='get',data='',charset='gbk')




a=[['剑来1', '剑来2', '剑来3'], ['烽火戏诸侯', '老油条本尊', '暮鼓晨钟']]
b=['bookName','bookAuthor']

c=[dict(zip(b,i) for i in zip(*a))]
print(c)
