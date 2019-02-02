from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

posts = [
    {
        'author': 'Vivekananthan',
        'title': 'Blog Post 1',
        'content': 'First Post Content',
        'date_posted': 'Jan 30, 2019'
    },
    {
        'author': 'Ambethkar',
        'title': 'Blog Post 2',
        'content' : 'Second Post Content',
        'date_posted' : 'Jan 31 2019'
    }
]

def home(request):
    context= {
        'posts' : posts
    }
    return render(request, 'blog/home.html',context)

def about(request):
    return render(request, 'blog/about.html')

def login (request):
    return render(request,'blog/login.html')
