from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

# Create your views here.
from .forms import PostForm
from .models import Post
#-----------------------------
def index(request):
    data=Post.objects.filter().order_by('-id')
    return render(request,'index.html',{'posts':data})
#------------------------------
def add(request):
    alert="";
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            title = request.POST.get('title', '')
            body = request.POST.get('body', '')
            resp=Post(title=title,body=body)
            resp.save()
            if resp.id != 0 :
                alert = "ثبت اطلاعات با موفقیت انجام شد"
            else:
                alert="متاسفانه ثبت اطلاعات انجام نشد"
    else:
        form = PostForm()
    return render(request, 'add.html', {'form': form,'alert':alert})
#------------------------------
def update(request,id):
    alert="";
    instance = get_object_or_404(Post, id=id)
    form = PostForm(request.POST or None, instance=instance)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            alert = "ویرایش اطلاعات با موفقیت انجام شد"
        else:
            alert="اطلاعات وارد شده صحیح نمی باشد"
    return render(request, 'update.html', {'form': form,'alert':alert})
#------------------------------
def detail(request,id):
    data=Post.objects.filter(id=id).all()
    return render(request,'detail.html',{"posts":data})
#------------------------------
def list(request):
    return render(request,'list.html',)