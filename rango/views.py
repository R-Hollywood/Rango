from django.shortcuts import render
from django.http import HttpResponse

def index(request):
     context_dict = {'boldmessage': "Crunchy, creamy, cookie, candy, cupcake!"}
     html="Welcome page" +'<a href="/rango/about/">About</a>'
     return render(request,'rango/index.html',context=context_dict)

def about(request):
    html="About page" + '<a href="/rango/">Index</a>'
    return HttpResponse(html)
