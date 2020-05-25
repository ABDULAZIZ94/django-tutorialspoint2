from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

def hello2(request):
   text = """<h1>welcome to my app !</h1>"""
   return HttpResponse(text)
# Create your views here.

def hello(request):
   return render(request, "hello.html", {})
