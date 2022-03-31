from django.shortcuts import render
from django.http import HttpRequest
from django.http import HttpResponse
# Create your views here.
"""
视图
所谓的视图 其实就是Python函数
视图函数有2个要求：
    1.第一个参数就是接收请求。就是HttpRequest的类对象
    2.必须返回一个响应
"""


# 用户输入http://127.0.0.1:8000/index/ 来访问视图函数
def index(request):

    # return HttpResponse('ok')
    # render() 渲染模板
    # request, template_name, context=None
    # request,   请求
    # template_name,  磨板名字
    # context=   数据库动态数据
    context = {'name': '这是动态数据223'}
    return render(request, 'book/index.html', context=context)
