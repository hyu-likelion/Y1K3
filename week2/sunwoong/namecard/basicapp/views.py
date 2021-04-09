from django.shortcuts import render

# Create your views here.
def namecard(request):
    return render(request, "namecard.html")
