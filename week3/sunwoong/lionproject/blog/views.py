from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.core.paginator import Paginator
from .models import Blog

# Read
def home(request):
    blogs = Blog.objects.order_by('-pub_date')

    search = request.GET.get('search')
    if search == 'true':
        writer = request.GET.get('writer')
        blogs = Blog.objects.filter(writer=writer)
        # return render(request, "home.html", {"blogs": blogs})

    paginator = Paginator(blogs, 3) # 3개씩 쪼개서 보내기
    page = request.GET.get('page')
    blogs = paginator.get_page(page)
    return render(request, "home.html", {"blogs": blogs})


def detail(request, id):
    # 가져오든가 없으면 404 에러 띄우기.
    blog = get_object_or_404(Blog, pk=id)
    return render(request, 'detail.html', {"blog": blog})


# Create
def new(request):
    return render(request, 'new.html')


def create(request):
    new_blog = Blog()

    new_blog.title = request.POST['title']
    new_blog.writer = request.POST['writer']
    new_blog.body = request.POST['body']
    new_blog.pub_date = timezone.now()
    
    new_blog.save()
    return redirect('detail', new_blog.id)


# Update
def edit(request, id):
    edit_blog = Blog.objects.get(id=id)
    return render(request, 'edit.html', {'blog': edit_blog})


def update(request, id):
    update_blog = Blog.objects.get(id=id)
    update_blog.title = request.POST['title']
    update_blog.writer = request.POST['writer']
    update_blog.body = request.POST['body']
    update_blog.pub_date = timezone.now()

    update_blog.save()
    return redirect('detail', update_blog.id)


# Delete
def delete(request, id):
    delete_blog = Blog.objects.get(id=id)
    delete_blog.delete()
    return redirect('home')