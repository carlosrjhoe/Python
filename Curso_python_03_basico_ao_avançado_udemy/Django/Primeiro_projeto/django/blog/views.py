from django.shortcuts import render
from blog.data import posts

# Create your views here.
def index(request):
    
    context = {
        'posts': posts
    }
    
    return render(request, 'blog/index.html', context)