from django.shortcuts import render
from django.shortcuts import redirect
from .models import Question as db

reply = []
question_cnt = 0
question_total = 0

# Create your views here.
def main(request):
    global question_cnt, question_total
    
    questions = db.objects.all()
    question_total = len(questions)

    return render(request, "main.html", {"total_num": question_total, "cnt": question_cnt+1, "question": questions[question_cnt]})


def complete(request):
    global reply, question_cnt, question_total

    reply.append(request.GET["reply"])

    if question_cnt < question_total-1:
        question_cnt += 1
        return redirect("main")
    else:
        i = 0
        for question in db.objects.values():
            reply[i] = [question['question'], reply[i]]
            i += 1

        temp = render(request, "complete.html", {"reply": reply})
        question_cnt = 0
        reply = []
        return temp