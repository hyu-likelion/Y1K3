from django.shortcuts import render,redirect
from list.models import Todo
# Create your views here.

def home(request):
    todo_list = Todo.objects.all()
    return render(request,"home.html",{'todo_list':todo_list})

def edit(request,id):
    edit_list = Todo.objects.get(id=id)
    return render(request,'edit.html',{'list':edit_list})

def detail(request, id):
    detail_list = get_object_or_404(Todo, pk = id)
    return render(request,'detail.html',{'list':detail_list})

def new(request):
    return render(request,'new.html')

def create(request):
    new_list = Todo()
    new_list.body = request.POST['body']
    new_list.save()
    return redirect('home')

def edit(request,id):
    edit_list = Todo.objects.get(id=id)
    return render(request,'edit.html',{'list':edit_list})

def update(request,id):
    update_list = Todo.objects.get(id=id)
    update_list.body = request.POST['body']
    update_list.save()
    return redirect('home')

def delete(request,id):
    delete_list=Todo.objects.get(id=id)
    delete_list.delete()
    return redirect('home')
