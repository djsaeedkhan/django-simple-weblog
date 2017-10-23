from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from .forms import PostForm
from .models import Post

def index(request):
    return render(request,'index.html',context=None)

def add(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            title = request.POST.get('title', '')
            body = request.POST.get('body', '')
            Post(title=title,body=body).save()
    else:
        form = PostForm()
    return render(request, 'add.html', {'form': form})

def list(request):
    return render(request,'list.html',)