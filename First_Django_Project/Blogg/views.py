from django.shortcuts import render

# create your views here
def home(request):
    return render(request, 'Blogg/home.html')

def about(request):
    return render(request, 'Blogg/about.html')
