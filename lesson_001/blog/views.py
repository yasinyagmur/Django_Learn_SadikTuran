from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("homepage")


def blogs(request):
    return HttpResponse("blogs")


def blog_details(request,id):
    return HttpResponse("blog details"+ str(id))
    