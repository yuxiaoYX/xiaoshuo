from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from .models import bookUser, bookSearch
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
