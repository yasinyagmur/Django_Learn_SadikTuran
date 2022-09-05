from . import views
from django.urls import path
urlpatterns = [
    path("",views.index),
    path("index",views.index),
    path("blogs",views.blogs),
    path("blogs/<int:id>",views.blog_details),
]
