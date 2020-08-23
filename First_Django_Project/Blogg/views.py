from django.shortcuts import render
from .models import Post

# create your views here
def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'Blogg/home.html', context)

def about(request):
    return render(request, 'Blogg/about.html')
