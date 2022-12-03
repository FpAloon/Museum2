
from django.shortcuts import render
from .models import *


def post_list(request):
    posts = Post.objects.filter()
    return render(request, 'blog/post_list.html', {'posts':posts})
