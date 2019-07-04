from django.urls import path
from . import views

urlpatterns=[
    path('',views.index,name='index'),
    path('search/',views.search,name='search'),
    path('introduce/',views.introduce,name='introduce'),
    path('booklist/',views.booklist,name='booklist'),
    path('content/',views.content,name='content')
]