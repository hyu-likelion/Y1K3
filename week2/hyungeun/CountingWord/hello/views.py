from django.shortcuts import render

def hello(request):
    return render(request, "hello.html")

def name(request):
    userName = request.GET['name']
    return render(request, "name.html", {"userName": userName})
