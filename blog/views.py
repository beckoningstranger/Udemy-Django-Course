from django.urls import reverse
from django.http import HttpResponse, Http404
from django.shortcuts import render


# Create your views here.
def index(request):
    return (HttpResponse('You reached index().'))


def url_handler(request, url_part):
    match(url_part):
        case "posts":
            return (HttpResponse('You reached posts().'))
        case _:
            raise Http404('404')

def show_blog_posts(request, slug):
    match(slug):
        case "1":
            return (HttpResponse('one'))
        case "2":
            return (HttpResponse('two'))
        case "3":
            return (HttpResponse('three'))
        case _:
            raise Http404()