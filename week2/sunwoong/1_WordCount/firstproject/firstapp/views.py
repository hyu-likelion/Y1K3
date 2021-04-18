from django.shortcuts import render

def welcome(request):
    #      render( default, 띄어주는 페이지 )
    return render(request, "welcome.html")

def hello(request):
    userName = request.GET["name"]
    return render(request, "hello.html", {'userName' : userName})