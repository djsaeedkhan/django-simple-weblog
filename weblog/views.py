from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

# Create your views here.
from .forms import PostForm
from .models import Post
#-----------------------------
def index(request):
    tag=""
    if request.method == 'GET' and request.GET.get("title") and  request.GET.get("title")!="":
        tag = request.GET.get("title")
        data = Post.objects.filter(title__icontains =tag).order_by('-id')
    else:
        data=Post.objects.filter().order_by('-id')

    return render(request,'index.html',{'posts':data,"tag":tag})
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
            return HttpResponseRedirect("/weblog/detail/"+id+"/")
            alert = "ویرایش اطلاعات با موفقیت انجام شد"
        else:
            alert="اطلاعات وارد شده صحیح نمی باشد"
    return render(request, 'update.html', {'form': form,'alert':alert})
#------------------------------
def detail(request,id):
    data=Post.objects.filter(id=id).all()
    return render(request,'detail.html',{"posts":data})
#------------------------------
def delete(request,id):
    data=Post.objects.filter(id=id).all()
    data.delete()
    return HttpResponseRedirect("/weblog/")
#------------------------------
def list(request):
    return render(request,'list.html',)