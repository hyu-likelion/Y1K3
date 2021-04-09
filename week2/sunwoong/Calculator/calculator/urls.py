from django.urls import path
from . import views

urlpatterns = [
    # 메인페이지 url
    path('main/', views.main, name="main"),
    # calculator 페이지 url
    path('result/', views.calculator, name="result"),
]