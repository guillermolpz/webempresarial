from inspect import BlockFinder
from django.shortcuts import render

#from blog.models import Blog
from .models import Blog

# Create your views here.
def blog(request):
    blogs = Blog.objects.all()
    return render(request, 'blog.html', {'blogs':blogs})
