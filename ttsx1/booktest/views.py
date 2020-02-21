from django.shortcuts import render
from .models import *
from django.db.models import Max,F,Q

# Create your views here.

def index(request):
    # list=BookInfo.books1.filter(heroinfo__hcontent__contains='八')  #跨关联关系的查询：处理join查询
    # list=BookInfo.books1.filter(id__lte=3)
    # max=BookInfo.books1.aggregate(Max('bpub_date'))   #聚合函数
    # list=BookInfo.books1.filter(bread__lt=F('bcommet'))    #•可以使用模型的字段A与字段B进行比较
    # list=BookInfo.books1.filter(id__gte=6,btitle__contains='八')  #逻辑与的关系
    # list=BookInfo.books1.filter(id__gt=6).filter(btitle__contains='八')  #逻辑与的关系，等价于上面一条
    list=BookInfo.books1.filter(Q(id__gt=6) | Q(btitle__contains='八'))  #逻辑或的关系
    context={'list1':list
             # ,'max1':max
             }
    return render(request,'booktest/index.html',context)
