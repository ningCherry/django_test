from django.http import HttpResponse
from django.utils.deprecation import MiddlewareMixin

#出错原始代码：
# from django.http import HttpResponse
# class MyException(object):
#     def process_exception(request,response, exception):
#         return HttpResponse(exception.message)


# #正确代码1
# class MyException(object):
#     def __init__(self, get_response):
#         self.get_response = get_response
#
#     def __call__(self, request):
#         return self.get_response(request)
#
#     def process_exception(self, request, exception):
#         return HttpResponse(exception)
#

#正确代码2
from django.http import HttpResponse
from django.utils.deprecation import MiddlewareMixin

class MyException(MiddlewareMixin):
    def process_exception(self, request, exception):
        return HttpResponse(exception)