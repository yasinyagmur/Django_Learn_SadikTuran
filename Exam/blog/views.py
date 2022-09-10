from datetime import date
from inspect import BlockFinder
from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Blog,Category


# Create your views here.
def index(request):
    context={
        # "blogs":data["blogs"]
        "blogs":Blog.objects.filter(is_home=True,is_activate=True),
        "category":Category.objects.all()
    }
    return render(request,"blog/index.html",context)


def blogs(request):
    context={
        # "blogs":data["blogs"]
        "blogs":Blog.objects.filter(is_activate=True),
        "category":Category.objects.all()

    }
    return render(request,"blog/blogs.html",context)



def blog_details(request,slug):
    # blogs=data["blogs"]
    # selectedblog=None
    
    # for blog in blogs:
    #     if blog["id"]==id:
    #         selectedblog=blog
    blog=Blog.objects.get(slug=slug)
    # selectedblog =[ blog for blog in blogs if blog["id"]==id][0]

    return render(request,"blog/blog-details.html",{
        # "blog":selectedblog
        "blog":blog
    })
    


def blog_by_category(request,slug):
    pass