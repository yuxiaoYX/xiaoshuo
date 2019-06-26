from django.contrib import admin
from .models import bookUser, bookSearch
# Register your models here.


class userAdmin(admin.ModelAdmin):
    fields = ['userName', 'password', 'bookrack']


admin.site.register(bookUser, userAdmin)


class searchAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['source_name']}),
        ('源搜索访问规则', {'fields': ['requests_url', 'requests_method', 'requests_data', 'requests_charset']}),
        ('源搜索过滤规则', {'fields': ['search_key', 'search_value']})
    ]

admin.site.register(bookSearch, searchAdmin)
