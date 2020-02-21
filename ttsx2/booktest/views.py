from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect

# Create your views here.

def index(request):
    return HttpResponse('hello cherry!')

def detail(request,p):
    return HttpResponse(p)

def detail1(request,p1,p2,p3):
    return HttpResponse('years-{},month-{},day-{}'.format(p1,p2,p3))


#get属性练习
#展示链接的页面
def getTest1(request):
    return render(request,'booktest/getTest1.html')

#接收一键一值得情况
def getTest2(request):
    # 根据键接收值
    a1=request.GET['a']     #只能获取键的一个值
    b1=request.GET['b']
    c1=request.GET['c']
    #构造上下文
    context={'a':a1,'b':b1,'c':c1}
    #向模板中传递上下文，并进行渲染
    return render(request,'booktest/getTest2.html',context)

#接收一键多值得情况
def getTest3(request):
    a1=request.GET.getlist('a')    #getlist()：根据键获取值，将键的值以列表返回，可以获取一个键的多个值
    context={'a':a1}
    return render(request,'booktest/getTest3.html',context)


#post属性练习
def postTest1(request):
    return render(request,'booktest/postTest1.html')

def postTest2(request):
    name=request.POST['uname']   #获取uname的值
    pwd=request.POST['upwd']
    gender=request.POST.get('ugender')     #等价于request.Post['ugender']
    hobby=request.POST.getlist('uhobby')   #获取uhhoby所有值
    context={'name':name,'pwd':pwd,'gender':gender,'hobby':hobby}
    return render(request,'booktest/postTest2.html',context)


#cookie练习
def cookieTest(request):
    response=HttpResponse()
    cookie=request.COOKIES    #获取所有cookie信息
    if 't1' in cookie:   #判断cookie是否有键t1
        response.write(cookie['t1'])  #如果有则获取t1的值
    else:
        response.set_cookie('t1','abc')  #如果没有则设置Cookie
    return response


#重定向练习
def redTest1(request):
    # return HttpResponseRedirect('/booktest/redTest2/')
    return redirect('/booktest/redTest2/')
def redTest2(request):
    return HttpResponse('这是重定向的页面')


#通过用户登录练习session
#首页
def session1(request):
    # uname=request.session['uname']  #没获取到uname的值会报错
    uname=request.session.get('uname','未登录')   #根据键获取会话的值，没获取到uname的值不会报错
    context={'uname':uname}
    return render(request,'booktest/session1.html',context)
#登录页
def session2(request):
    return render(request,'booktest/session2.html')
def session2_handle(request):
    uname=request.POST['uname']  #获取uname的值
    request.session['uname']=uname   #设置session
    # request.session.set_expiry(0)    #设置会话的超时时间,value为0，那么用户会话的Cookie将在用户的浏览器关闭时过期
    return redirect('/booktest/session1/')   #重定向
#退出
def session3(request):
    #删除session
    del request.session['uname']
    return redirect('/booktest/session1/')