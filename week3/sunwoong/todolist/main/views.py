from django.shortcuts import render, redirect
from .models import Todo
from .forms import TodoForm

# Create your views here.
def main(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('main')
    else:
        form = TodoForm()
        todos = Todo.objects.all()
        return render(request, 'main.html', {"todos": todos, 'form': form})


def update(request, id):
    todo = Todo.objects.get(id=id)

    if request.method == 'POST':
        form = TodoForm(request.POST)
        form.save()
        return redirect('main')
    else:
        return render(request, 'update.html', {'todo': todo})


def delete(request, id):
    delete_todo = Todo.objects.get(id=id)
    delete_todo.delete()
    return redirect('main')