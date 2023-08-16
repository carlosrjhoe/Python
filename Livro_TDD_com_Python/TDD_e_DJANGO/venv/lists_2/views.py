from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'lists_2/index_lists_2.html')
