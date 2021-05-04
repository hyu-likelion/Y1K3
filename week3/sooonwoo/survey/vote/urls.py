from django.urls import path

from vote import views

urlpatterns = [
    path('', views.home, name= "home"),
    path('question',views.question, name="question"),
    path('save_survey',views.save_survey, name = "save_survey"),
    path('show_result/<int:question_id>', views.show_result, name="result"),
]
