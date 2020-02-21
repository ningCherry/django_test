from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.conf import settings
import os
from django.core.paginator import Paginator
from .models import *

# Create your views here.

def index(request):
    return render(request,'booktest/index.html')

def myExc(request):
    a=int('abc')
    return HttpResponse(a)


#文件上传练习
def uploadPic(request):
    return render(request,'booktest/uploadPic.html')

def uploadHandle(request):
    file=request.FILES['pic1']   #获取上传的文件
    filepathname=os.path.join(settings.MEDIA_ROOT,file.name)  #拼接上传文件的路径
    with open(filepathname,'wb+') as pic:
        for c in file.chunks():       #在file.chunks()上循环而不是用read()保证大文件不会大量使用系统内存
            pic.write(c)
    # return HttpResponse(filepathname)
    return HttpResponse('<img src="/static/media/{}">'.format(file.name))  #返回上传的图片


#进行分页练习
def herolist(request,pindex):
    if pindex=='':
        pindex=1
    list=HeroInfo.objects.all()
    pageinator=Paginator(list,5)
    page=pageinator.page(pindex)
    context={'page':page}
    return render(request,'booktest/herolist.html',context)


#省市区选择
def area(request):
    return render(request,'booktest/area.html')

def area2(request,id):
    id1=int(id)
    if id1==0:
        data=AreaInfo.objects.filter(parea__isnull=True)  #获取省的数据
    else:
        data=[{}]
    list=[]
    for area in data:
        list.append([area.id,area.title])
    data1={'data':list}
    return JsonResponse(data1)   #查询信息，构造并返回json