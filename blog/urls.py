from django.urls import path
from . import views

urlpatterns = [
    path("", views.starting_page, name="starting-page"),
    path("blog/posts", views.posts, name="posts-page"),
    path("blog/posts/<slug:slug>", views.post_detail, name="posts-detail-page"),
]
