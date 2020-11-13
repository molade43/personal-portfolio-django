from django.shortcuts import render, get_object_or_404
from .models import Blog

# Create your views here.


def all_blogs(request):
    # this import all the datebase by using .all()
    blogs = Blog.objects.order_by('-date')
# this imports limited database by using .order_by('-date') [:5]
# blogs = Blog.object.order_by('-date')
    return render(request, 'blog/all_blogs.html', {'blogs': blogs})


def detail(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/detail.html', {'blog': blog})
