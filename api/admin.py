from django.contrib import admin
# from .models import bookUser, bookSearch, bookIntroduce,bookList,bookContent
# # Register your models here.


# class userAdmin(admin.ModelAdmin):
#     fields = ['userName', 'password', 'bookrack']


# admin.site.register(bookUser, userAdmin)


# class searchAdmin(admin.ModelAdmin):
#     fieldsets = [
#         (None, {'fields': ['source_name']}),
#         ('源搜索访问规则', {'fields': [
#          'requests_url', 'requests_method', 'requests_data', 'requests_charset']}),
#         ('源搜索过滤规则', {'fields': ['search_key', 'search_value']})
#     ]


# admin.site.register(bookSearch, searchAdmin)


# class introduceAdmin(admin.ModelAdmin):
#     fieldsets = [
#         ('源小说介绍', {'fields': ['source_name']}),
#         ('源小说介绍访问规则', {'fields': [
#          'requests_method', 'requests_data', 'requests_charset']}),
#         ('源小说介绍过滤规则', {'fields': ['introduce_key', 'introduce_value']})
#     ]


# admin.site.register(bookIntroduce, introduceAdmin)

# class listAdmin(admin.ModelAdmin):
#     fieldsets = [
#         ('源小说列表', {'fields': ['source_name']}),
#         ('源小说列表访问规则', {'fields': [
#          'requests_url','requests_method', 'requests_data', 'requests_charset']}),
#         ('源小说列表正则', {'fields': ['list_kv']})
#     ]


# admin.site.register(bookList, listAdmin)


# class contentAdmin(admin.ModelAdmin):
#     fieldsets = [
#         ('源小说章节内容', {'fields': ['source_name']}),
#         ('源小说章节内容访问规则', {'fields': [
#          'requests_method', 'requests_data', 'requests_charset']}),
#         ('源小说章节内容正则', {'fields': ['content_kv']})
#     ]


# admin.site.register(bookContent, contentAdmin)