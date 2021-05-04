from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect

from vote.models import Survey, Answer

# Create your views here.


def home(request):
    return render(request,"home.html")

def question(request):
    idx = int(request.GET["idx"])
    survey = Survey.objects.all()[idx]
    return render(request,"question.html",{'survey':survey})

def save_survey(request):
    # home.html의 form 을 통해 survey_idx를 받음.
    survey_idx = request.GET["survey_idx"]

    dto = Answer.objects.create(survey_idx=int(request.GET["survey_idx"]),ans=request.GET["num"])
    dto.save()
    return render(request, "success.html")

def show_result(request, question_id):
    result = Answer.objects.filter(survey_idx=question_id)
    return render(request, "result.html", {'result': result})
