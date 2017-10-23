from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from .forms import PostForm


def index(request):
    return render(request,'index.html',context=None)

def add(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            return HttpResponse('ok')
    else:
        form = PostForm()
    return render(request, 'add.html', {'form': form})

def list(request):
    return render(request,'list.html',)