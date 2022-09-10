from . import views
from django.urls import path
urlpatterns = [
    path("",views.index,name="home"),
    path("index",views.index),
    path("blogs",views.blogs,name="blogs"),
    path("category/<slug:slug>",views.blog_by_category,name="blog_by_category"),
    path("blogs/<slug:slug>",views.blog_details,name="blog_details"),
]
