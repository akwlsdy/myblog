# Create your views here.
from django.shortcuts import render
from .models import Post

def post_list(request):
    posts = Post.objects.all()  # 获取所有帖子
    return render(request, 'blog/post_list.html', {'posts': posts})
