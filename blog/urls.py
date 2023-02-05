from django.urls import path
from . import views

urlpatterns = [
    path("blogpost/home",views.home,name='blogHome'),
    path("", views.index, name="blogHome"),
    path("blogpost/blogpost/blogpost/blogpost/blogpost/blogpost/blog/<int:id>/", views.blogpost, name="blogHome"),
    # path('postComment', views.postComment, name="postComment"),
    path("blogpost/blogpst/search/?query=vishal/",views.search,name="search")
]
