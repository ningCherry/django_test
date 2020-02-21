from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(BookInfo)     #使用方式二：注册装饰器
class BookInfoAdmin(admin.ModelAdmin):
    list_display = ['id','btitle','bpub_date']

# admin.site.register(BookInfo,BookInfoAdmin)   #使用方式一：注册参数