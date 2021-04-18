from django.urls import path
from . import views


urlpatterns = [
# 메인페이지 url
    path('',views.main, name = "main"),
# calculator 페이지 url
    path('calculator',views.calculator,name="calculator"),
]
