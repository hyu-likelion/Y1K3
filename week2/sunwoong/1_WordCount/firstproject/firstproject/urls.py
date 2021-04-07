"""firstproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

# from firstapp import views
# import firstapp.views
from firstapp import views as first
from wordCount import views as wc

urlpatterns = [
    path('admin/', admin.site.urls),

    # ===============================================
    # First app
    # '' : 최초의 페이지가 이 페이지!
    # name : url 대신에 연결할 수 있는 nickname
    path('', first.welcome, name="welcome"),

    # path마다 url 주소는 다 달라야 함!
    path('hello/', first.hello, name="hello"),

    # ===============================================
    # WordCount app 
    path('wc/', wc.home, name="wc"),
    path('wc/result/', wc.result, name="result"),

]
