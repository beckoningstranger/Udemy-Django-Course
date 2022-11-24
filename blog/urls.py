from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<url_part>", views.url_handler, name="url_handler"),
    path("posts/<slug>", views.show_blog_posts, name="blog_posts"),
]