from django.shortcuts import render
from .models import *
from django.http import HttpResponse,JsonResponse
from django.views.decorators.cache import cache_page
from django.core.cache import cache
from .task import *

# Create your views here.

#----使用ajax完成省市区选择---
def index(request):
    return render(request,'booktest/index.html')

#省的信息
def pro(request):
    data=AreaInfo.objects.filter(parea__isnull=True)
    list=[]
    #[[1,北京],[2,河北],...]
    for pro in data:
        list.append([pro.id,pro.title])
    return JsonResponse({'data':list})

#市和区的信息
def city(request,id):
    data=AreaInfo.objects.filter(parea_id=id)
    list=[]
    #[{id:1,title:北京},{id:2,title:河北},...]
    for city in data:
        list.append({'id':city.id,'title':city.title})
    return JsonResponse({'data':list})


#----自定义富文本编辑器---
def content(request):
    return render(request,'booktest/content.html')

def content_handle(request):
    htmltext = request.POST['hcontent']  # 获取页面表单提交hcontent的值
    #修改字段值
    # data = TextTest.objects.get(pk=1)   #获取数据库TextTest主键为1的对象
    # data.hcontent=htmltext
    # data.save()   #将修改字段值保存至数据库
    #新增字段值
    data=TextTest()
    data.hcontent=htmltext
    data.save()
    context={'htmltext':htmltext}
    return render(request,'booktest/content_handle.html',context)


#设置redis缓存
# @cache_page(60*10)   #---单个view缓存---，使用装饰器，用于对视图的输出进行缓存。缓存十分钟
def cache1(request):
    # return HttpResponse('cherry')
    # return HttpResponse('cherry1')

    # cache.set('key1','value1',600)  #----设置缓存数据----
    # print(cache.get('key1'))   #获取缓存数据
    # return render(request,'booktest/cache1.html')   #cache1.html---模板片断缓存----

    cache.clear()  #清空缓存
    return HttpResponse('ok!')


#全文检索+中文分词
def mysearch(request):
    return render(request,'booktest/mysearch.html')


#celery异步
def celeryTest(request):
    # sayhello()   #直接调用
    sayhello.delay()   #异步调用
    HttpResponse('ok')