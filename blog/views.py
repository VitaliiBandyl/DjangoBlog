from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def posts_list(requests):
    return HttpResponse("<h1>Hello world </h>")
