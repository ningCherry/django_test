from django.contrib import admin
from .models import *

# Register your models here.
class HeroInfoInline(admin.TabularInline):   #关联注册
    model = HeroInfo
    extra = 2

# @admin.register(BookInfo)     #使用方式二：注册装饰器
class BookInfoAdmin(admin.ModelAdmin):
    list_display = ['id','btitle','bpub_date']    #显示字段，可以点击列头进行排序
    list_filter = ['btitle']      #过滤字段，过滤框会出现在右侧
    search_fields = ['btitle']     #搜索字段，搜索框会出现在上侧
    list_per_page = 10              #分页，分页框会出现在下侧
    fieldsets = [              #fieldsets：属性分组
        ('basic',{'fields':['btitle']}),
        ('more',{'fields':['bpub_date']})
    ]
    inlines = [HeroInfoInline]

admin.site.register(BookInfo,BookInfoAdmin)  #使用方式一：注册参数
admin.site.register(HeroInfo)