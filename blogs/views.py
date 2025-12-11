from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Blog,Category

# Create your views here.

def post_by_category(request,category_id):
    posts=Blog.objects.filter(status='published',category=category_id)
    try:
        categoy=Category.objects.get(pk=category_id)
    except:
        return redirect('home')
    context = {
        'posts':posts,
        'categoy':categoy,
    }
    return render(request, 'posts_by_category.html',context)