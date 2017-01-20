from django.shortcuts import render
from django.http import HttpResponse

def index(request):
 html="Welcome page" +'<a href="/rango/about/">About</a>'
 return HttpResponse(html)


def about(request):
    html="About page" + '<a href="/rango/">Index</a>'
    return HttpResponse(html)
