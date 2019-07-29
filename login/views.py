from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import User
# Create your views here.
import json
import time
# from django.contrib.sessions.models import Session
import random,string

def log_in(func):
    def wrapper(request, *args, **kwargs):
        token_value = json.loads(request.body).get('yz_token')  # 获取token值
        print(request.body)
        if not token_value:  #判断是否有token值
            return JsonResponse({"state":1,"errorMsg":"请登录！"})   #如果没有登录返回错误信息

        user=User.objects.filter(token=token_value)
        if not user:  #判断token是否和数据库中的匹配
            return JsonResponse({"state":1,"errorMsg":"请登录！"})   #如果没有登录返回错误信息
        return func(request, *args, **kwargs)  # 如果已经登录返回原函数请求页面
    return wrapper



def index(request):#登录
    if request.method == "POST":
        post_datas=json.loads(request.body)
        username=post_datas.get('username')
        password=post_datas.get('password')
        if not username or not password:
            return JsonResponse({"state":1,"errorMsg":"用户名或密码不能为空"})

        user = User.objects.filter(username=username, password=password)
        if user:
            # 生成随机token字符串，并保存到数据库中
            yz_token=''.join(random.choices(string.ascii_letters + string.digits, k=16))
            user.update(token=yz_token)

            return JsonResponse({"state":0,"errorMsg":"登录成功！","yz_token":yz_token})
        return JsonResponse({"state":1,"errorMsg":"账号或密码错误"})
    # 如果是GET请求，就说明是用户刚开始登录，使用URL直接进入登录页面的
    return HttpResponse('登录方式出错，请使用post')

def register(request):#注册
    if request.method == "POST":
        post_datas=json.loads(request.body)
        username=post_datas['username']
        password=post_datas['password']
        
        # register_user=User.objects.get_or_create(username=username,password=password)
        #注册前，先判断账号是否存在，然后再把用户名密码保存到数据表
        register_user=User.objects.filter(username=username)
        if register_user:
            return JsonResponse({"state":1,"errorMsg":"账号已存在，请更换！"})
        else:
            create_time=str(time.time())[:10]#取十位时间戳
            User.objects.create(username=username,password=password,create_time=create_time)
            
        return JsonResponse({"state":0,"errorMsg":"注册成功！"})

    return HttpResponse('登录方式出错，请使用post')


@log_in
def logout(request):#注销
    # 1.清理session某个值
    # try:
    #     del request.session['is_login']
    # except KeyError:
    #     pass

    # 2.清理所有session数据
    # request.session.clear()
    if request.method == "POST":
        token_value=json.loads(request.body)['yz_token']
        User.objects.filter(token=token_value).update(token=None)
        return HttpResponse('退出登录成功！')
    return HttpResponse('访问方式出错，请使用post')

#首页书架
@log_in
def bookrack(request):
    print(request.body)
    if request.method == "POST":
        token_value=json.loads(request.body)['yz_token']
        book_rack=User.objects.filter(token=token_value).values('bookrack')
        book_rack=book_rack[0]["bookrack"]
        book_rack=json.loads(book_rack)
        # print(type(book_rack[0]))

        return JsonResponse({"state":0,"errorMsg":"书架读取成功！","book_rack":book_rack},charset='utf-8')
        

    return HttpResponse('登录方式出错，请使用post')