from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime

def hello2(request):
   text = """<h1>welcome to my app !</h1>"""
   return HttpResponse(text)
# Create your views here.

def hello3(request):
   return render(request, "hello.html", {})

def hello4(request):
   today = datetime.now().date()
   return render(request, "hello.html", {"today" : today})

def hello(request):
   today = datetime.now().date()
   
   daysOfWeek = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
   return render(request, "hello2.html", {"today" : today, "days_of_week" : daysOfWeek})

