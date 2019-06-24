from django.contrib import admin
from .models import bookUser
# Register your models here.


class userAdmin(admin.ModelAdmin):
    fields = ['userName', 'password','bookrack']

admin.site.register(bookUser, userAdmin)