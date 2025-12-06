from django.shortcuts import render,get_object_or_404
from blogs.models import Blog, Category
from django.http import HttpResponse
from assignments.models import About

def home(request):
    categories = Category.objects.all()
    blogs = Blog.objects.filter(is_featured=True)
    sample_posts = Blog.objects.filter(is_featured=False,status='published')
    about = About.objects.get()
    context = {
        'categories' : categories,
        'blogs':blogs,
        'sample_posts' :sample_posts,
        'about':about,
    }
    return render(request,'home.html',context)


    