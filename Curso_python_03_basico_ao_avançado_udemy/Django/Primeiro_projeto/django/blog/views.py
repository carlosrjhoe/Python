from django.http import Http404
from django.shortcuts import render
from blog.data import posts

# Create your views here.
def index(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/index.html', context)

def post(request, id):

    found_post = None

    for post in posts:
        if post['id'] == id:
            found_post = post
            break

    if found_post is None:
        raise Http404('Post not found')
    
    context = {
        'post': found_post,
        'title': found_post['title']
    }
    return render(request, 'blog/post.html', context)