from django.shortcuts import redirect, render,get_object_or_404
from blog_main.forms import RegistrationForm
from blogs.models import Blog, Category
from django.http import HttpResponse
from assignments.models import About
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth

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

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('register')
        else:
            form.errors
    else:
        form = RegistrationForm()
        
        
    form = RegistrationForm()
    context = {
        'form' : form,
    }
    return render(request,'register.html',context)

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request,request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = auth.authenticate(request,username=username,password=password)
            if user is not None:
                auth.login(request,user)
            return redirect('home')
    form = AuthenticationForm()
    context = {
        'form':form,
    }
    return render(request,'login.html',context)

def logout(request):
    auth.logout(request)
    return redirect('home')

