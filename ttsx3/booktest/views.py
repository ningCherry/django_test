from django.shortcuts import render
from .models import *
from django.http import HttpResponse
# Create your views here.

#定义模板
def index(request):
    # herolist=HeroInfo.objects.get(pk=1)
    # context={'booklist':herolist}

    herolist=HeroInfo.objects.all()   #查询所有
    # herolist=HeroInfo.objects.filter(isDelete=True)   #过滤
    context={'herolist':herolist}
    return render(request,'booktest/index.html',context)

#反向解析
def show(request,id,id2):
    context={'id':id}
    return render(request,'booktest/show.html',context)


#练习模板的继承
def index2(request):
    return render(request,'booktest/index2.html')
def user1(request):
    context={'name':'cherry'}
    return render(request,'booktest/user1.html',context)
def user2(request):
    return render(request,'booktest/user2.html')


#html转义
def htmlTest(request):
    context={'t1':'<h1>abc</h1>'}
    return render(request,'booktest/htmlTest.html',context)


#csrf跨站请求伪造
def csrf1(request):
    return render(request,'booktest/csrf1.html')
def csrf2(request):
    uname=request.POST['uname']
    return HttpResponse(uname)    #HttpResponse不调用模板，直接返回数据


#验证码防止crsf练习
#--------------------自己创建图文验证码--------------------
#自己创建验证码
def verifyCode(request):
    from PIL import Image,ImageDraw,ImageFont
    import random
    #创建背景色
    bgColor=(random.randrange(50,100),random.randrange(50,100),0)
    #规定宽高
    width=100
    height=25
    #创建画布
    image=Image.new('RGB',(width,height),bgColor)
    #构造字体对象
    font=ImageFont.truetype('simkai.ttf',24)    #在Windows环境，字体一般位于C:\WINDOWS\Fonts文件夹下
    #创建画笔
    draw=ImageDraw.Draw(image)
    #创建文本内容
    text='1234ABCD'
    #逐个绘制文字：
    textTemp=''
    for i in range(4):
        textTemp1=text[random.randrange(0,len(text))]
        textTemp+=textTemp1
        draw.text((i*18,0),textTemp1,(255,255,255),font)
    #将验证码存至session
    request.session['code']=textTemp
    #保存至内存流中
    import io
    buf=io.BytesIO()
    image.save(buf,'png')
    #将内存流中的内容输出至客户端
    return HttpResponse(buf.getvalue(),'image/png')    #这里是重点，MIME类型为图片png

#验证码表单页
def verifyTest1(request):
    return render(request,'booktest/verifyTest1.html')

#判断验证码是否正确,将验证码的数据其实是存储到session中通过session和前端获取的值进行比较
def verifyTest2(request):
    code1=request.POST['code']
    code2=request.session['code']
    if code1==code2:
        return HttpResponse('ok')
    else:
        return HttpResponse('no')


#--------------------使用第三方captcha验证码--------------------
'''
第一步：安装包pip install django-simple-captcha
第二步：在setting.py中INSTALLED_APPS添加“captcha”这个app
第三步：在主路由urls.py配置captcha应用的路由，path('captcha/',include('captcha.urls'))
第四步：迁移同步，更新数据库，生成captcha所依赖的表，执行makemigrations和migrate
然后如下步骤：
'''

from captcha.fields import CaptchaField
from django import forms

# 创建一个表单的类，这里的captcha = CaptchaField()就是使用了captcha这个插件了
class RegisterForm(forms.Form):
    captcha = CaptchaField()

#验证码表单页
def verifyTest3(request):
    context={'code':RegisterForm()}   #RegisterForm()实例化表单
    return render(request,'booktest/verifyTest3.html',context)

#判断验证码是否正确
def verifyTest4(request):
    register_form = RegisterForm(request.POST)  #这里必须添加request.POST来获取提交的表单数据

    if register_form.is_valid():    #is_valid()用来判断是否返回值
        return HttpResponse('ok')
    else:
        return HttpResponse('no')