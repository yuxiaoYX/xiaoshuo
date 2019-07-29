from django.contrib import admin
from .models import User
# Register your models here.


class userAdmin(admin.ModelAdmin):
    fields = ['username', 'password', 'bookrack']


admin.site.register(User, userAdmin)