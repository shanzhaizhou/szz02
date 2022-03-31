from django.urls import path
from book.views import index

urlpatterns = [
    path('index/', index),  # path(路由，视图函数名)
]
