from django.shortcuts import render, redirect, render_to_response
from django.http import HttpResponse
import datetime
from myapp.forms import LoginForm
from django.template import RequestContext

# Create your views here.
def hello(request):
   today = datetime.datetime.now().date()
   daysOfWeek = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
   return render(request, "hello.html", {"today" : today})

def login(request):
   username = "not logged in"
   
   if request.method == "POST":
      #Get the posted form
      MyLoginForm = LoginForm(request.POST)
   
   if MyLoginForm.is_valid():
      username = MyLoginForm.cleaned_data['username']
   else:
      MyLoginForm = LoginForm()
   
   response = render_to_response(request, 'loggedin.html', {"username" : username}, context_instance = RequestContext(request))
   
   response.set_cookie('last_connection', datetime.datetime.now())
   response.set_cookie('username', datetime.datetime.now())
	
   return response

def formView(request):
   if 'username' in request.COOKIES and 'last_connection' in request.COOKIES:
      username = request.COOKIES['username']
      
      last_connection = request.COOKIES['last_connection']
      last_connection_time = datetime.datetime.strptime(last_connection[:-7], 
         "%Y-%m-%d %H:%M:%S")
      
      if (datetime.datetime.now() - last_connection_time).seconds < 10:
         return render(request, 'loggedin.html', {"username" : username})
      else:
         return render(request, 'login.html', {})
			
   else:
      return render(request, 'login.html', {})
