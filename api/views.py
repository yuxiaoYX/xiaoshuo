from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.core import serializers
from .models import bookUser, bookSearch,bookIntroduce,bookList,bookContent
import xiaoshuo1
import json

# Create your views here.

#没用
def index(request):
    data = serializers.serialize("json", bookUser.objects.all(), ensure_ascii=False)
    return HttpResponse(data, content_type="application/json,charset=utf-8")


def search(request):
    searchkey = request.GET.get('searchkey', default='')
    sourc_name = request.GET.get('source_name', default='')
    print(searchkey,sourc_name)
    if searchkey and sourc_name:
        search_data = xiaoshuo1.book_search(searchkey,sourc_name)
        print(search_data)
        # search_data={"提示":"正确"}
        return JsonResponse(search_data, safe=False)
        # return HttpResponse(json.dumps(search_data, ensure_ascii=False), content_type="application/json,charset=utf-8")
    else:
        return HttpResponse('没有该源')

def introduce(request):
    if request.method=='POST':
        post_data=json.loads(request.body)
        # book_data=bookIntroduce.objects.filter(source_name=post_data['source_name'])
        if post_data:
            introduce_data=xiaoshuo1.book_jieshao(post_data['url'],post_data['source_name'])
            return JsonResponse(introduce_data, safe=False)
            # return HttpResponse(json.dumps(introduce_data, ensure_ascii=False), content_type="application/json,charset=utf-8")
        else:
            return HttpResponse('没有该源')
    else:
        return HttpResponse('访问方式出错')
    

def booklist(request):
    listUrl = request.GET.get('listUrl', default='')
    sourc_name = request.GET.get('source', default='')
    # book_data=bookList.objects.filter(source_name=sourc_name)
    if listUrl and sourc_name:
        # book_data=book_data.values()[0]
        # book_data['requests_url']=book_data['requests_url']+listUrl
        list_data=xiaoshuo1.book_list(listUrl,sourc_name)
        # list_data={'list_data':json.dumps(list_data, ensure_ascii=False),'url':book_data['requests_url']}
        # list_data={"list_data":list_data}
        return JsonResponse(list_data, safe=False)
    else:
        return HttpResponse('访问方式出错')

def content(request):
    if request.method=='POST':
        post_data=json.loads(request.body)
        # book_data=bookContent.objects.filter(source_name=post_data['source_name'])
        if post_data:
            # book_data=book_data.values()[0]
            # book_data['requests_url']=post_data['chapterUrl']
            content_data=xiaoshuo1.book_content(post_data['chapterUrl'],post_data['source_name'])
            return JsonResponse([content_data],safe=False)
        else:
            return HttpResponse('没有该源')
    return HttpResponse('访问方式出错')


def list(request):
    pass