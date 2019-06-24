from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.core import serializers
from .models import bookUser
import xiaoshuo

# Create your views here.


def index(request):
    data = serializers.serialize("json",bookUser.objects.all(),ensure_ascii=False)
    return HttpResponse(data,content_type="application/json,charset=utf-8")


def search(request):


    return HttpResponse()