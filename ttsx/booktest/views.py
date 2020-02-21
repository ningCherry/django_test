from django.shortcuts import render
from django.http import *
from django.template import RequestContext,loader
from .models import *

# Create your views here.

def index(request):
    # temp=loader.get_template('booktest/index.html')  #加载模板
    # return HttpResponse(temp.render())   #将模板渲染出来
    booklist =BookInfo.objects.all()
    context={'list':booklist}
    return render(request,'booktest/index.html',context)   #可以使用这一句代替上面注释的两行代码，即此行代码就是封装了上面两行代码

def detail(request,id):
    book=BookInfo.objects.get(pk=id)  #获取某本书
    herolist=book.heroinfo_set.all   #获取某本书的所有英雄名
    context={'herolist':herolist}
    return render(request,'booktest/detail.html',context)