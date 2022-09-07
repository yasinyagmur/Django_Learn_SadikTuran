from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse


data={
    "blogs":[
        {
            "id":1,
            "title":"Web geliştirme",
            "image":"1.jpg",
            "is_activate":True,
            "is_home":False,
            "description":"Perfect Course"
        },
        {
            "id":2,
            "title":"Python geliştirme",
            "image":"2.jpg",
            "is_activate":True,
            "is_home":True,
            "description":"Perfect Course"
        },
        {
            "id":3,
            "title":"django geliştirme",
            "image":"3.jpg",
            "is_activate":False,
            "is_home":True,
            "description":"Perfect Course"
        }
    ]
}

# Create your views here.
def index(request):
    context={
        "blogs":data["blogs"]
    }
    return render(request,"blog/index.html",context)


def blogs(request):
    context={
        "blogs":data["blogs"]
    }
    return render(request,"blog/blogs.html",context)



def blog_details(request,id):
    context={
        "blogs":data["blogs"]
    }
    return render(request,"blog/blog-details.html",{
        "id":id
    })
    