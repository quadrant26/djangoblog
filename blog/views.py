from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post
from .forms import PostForm
from django.http import HttpRequest

#
from django.shortcuts import redirect

def runoob(request):
    context = {}
    context['hello'] = '绿杨烟外晓寒轻'
    views_name = "菜鸟教程"
    views_list = ["菜鸟1", "菜鸟2", "菜鸟3"]
    views_dict = { "name": "菜鸟教程"}
    num = 1024
    import datetime
    now = datetime.datetime.now()
    # return render(request, 'runoob.html', context)

    views_href = "<a href='https://www.runoob.com/'>点击跳转</a>"
    # return render(request, "runoob.html", {"views_href": views_href})

    views_num = 88
    return render(request, "runoob.html", {"views_list": views_list})

# Create your views here.
def hello(request):
    # return HttpRequest("Hello World!");
    return render(request, 'blog/hello.html')

def post_list(request):
    print(request);
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})


def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})