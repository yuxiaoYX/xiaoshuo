from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from .models import bookUser, bookSearch,bookIntroduce
import xiaoshuo1
import json

# Create your views here.


def index(request):
    data = serializers.serialize("json", bookUser.objects.all(), ensure_ascii=False)
    return HttpResponse(data, content_type="application/json,charset=utf-8")


def search(request):
    searchkey = request.GET.get('searchkey', default='')
    book_data = bookSearch.objects.filter(source_name='爱奇文学')
    if book_data:
        search_data = xiaoshuo1.book_search(searchkey, book_data.values()[0])
        # search_data = serializers.serialize("json", search_data, ensure_ascii=False)
        return HttpResponse(json.dumps(search_data, ensure_ascii=False), content_type="application/json,charset=utf-8")
    else:
        return HttpResponse('没有该源')

def introduce(request):
    if request.method=='POST':
        post_data=json.loads(request.body)
        book_data=bookIntroduce.objects.filter(source_name=post_data['source_name'])
        if book_data:
            book_data=book_data.values()[0]
            book_data['requests_url']=post_data['url']
            introduce_data=xiaoshuo1.book_jieshao(book_data)
            return HttpResponse(json.dumps(introduce_data, ensure_ascii=False), content_type="application/json,charset=utf-8")
        else:
            return HttpResponse('没有该源')
        return HttpResponse('没有该源')
    return HttpResponse('访问方式出错')
