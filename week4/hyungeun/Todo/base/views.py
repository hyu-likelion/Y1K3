from django.shortcuts import redirect, render
from .models import Todo
from .forms import ToDoForm

# Create your views here.

def home(request):
    if request.method == "POST":
        form = ToDoForm(request.POST or None)

        if(form.is_valid()):
            form.save()
            all_items = Todo.objects.all
            return render(request, 'home.html', {'all_items': all_items})
    else:
        all_items = Todo.objects.all
        return render(request, 'home.html', {"all_items":all_items})

def delete(request, id):
    deleteTask = Todo.objects.get(pk = id)
    deleteTask.delete()
    return redirect('home')

def cross_off(request, id):
    task = Todo.objects.get(pk = id)
    task.completed = True
    task.save()

    return redirect('home')

def uncross(request, id):
    task = Todo.objects.get(pk = id)
    task.completed = False
    task.save()

    return redirect('home')

def edit(request, id):
    if request.method == "POST":
        item = Todo.objects.get(pk = id)
        form = ToDoForm(request.POST or None, instance= item)

        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        task = Todo.objects.get(pk = id)
        return render(request, 'edit.html', {"task": task})

