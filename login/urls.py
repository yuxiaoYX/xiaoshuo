from django.urls import path
from . import views

urlpatterns=[
    path('',views.index,name='index'),
    path('register/',views.register),
    path('logout/',views.logout),
    path('bookrack/',views.bookrack)
]