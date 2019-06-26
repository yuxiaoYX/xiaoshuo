from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.core import serializers
from .models import bookUser,bookSearch
import xiaoshuo1
import json

# Create your views here.


def index(request):
    data = serializers.serialize("json",bookUser.objects.all(),ensure_ascii=False)
    return HttpResponse(data,content_type="application/json,charset=utf-8")


def search(request):
    searchkey=request.GET.get('aa',default='')
    book_data=bookSearch.objects.filter(source_name='爱奇文学')
    if book_data:
        book_datas=book_data.values()[0]
        print(book_datas)
        aa=book_datas['requests_data']
        print(aa)
        print(type(aa))
        cc=json.loads(book_datas['requests_data'])
        print(cc)
        json.loads(book_datas['requests_data'])['searchkey']=searchkey.encode(book_datas['requests_charset'])
        # xiaoshuo1.abc1()
    return HttpResponse('1')