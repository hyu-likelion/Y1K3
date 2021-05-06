from django.urls import path
from .views import cross_off, edit, home, delete, uncross

urlpatterns = [
    path('', home, name = 'home'),
    path('delete/<str:id>', delete, name = 'delete'),
    path('cross/<str:id>', cross_off, name = 'cross'),
    path('uncross/<str:id>', uncross, name = 'uncross'),
    path('edit/<str:id>', edit, name = 'edit')
]
