from asyncio.windows_events import NULL
from django.shortcuts import render, redirect
from datetime import datetime
from django.contrib import messages
from Develop.models import Contact
from .models import *
from .forms import NewUserForm
from django.contrib.auth import login, authenticate ,logout#add this
from django.contrib.auth.forms import AuthenticationForm #add this
# Create your views here.
def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        query = request.POST.get('query')
        
        Cont = Contact(name = name, email = email, phone = phone , query = query , date = datetime.now())
        
        if all([name, email, phone, query]) != NULL :
            Cont.save()
            messages.success(request, 'Your message has been sent..')
        else:
            messages.success(request, 'Please fill all the blanks')
    
    return render(request, 'contact.html')

def courses(request):
    return render(request, 'courses.html')

#login form
'''
def login_request(request):
	if request.method == "POST":
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			messages.info(request, f"You are now logged in as {username}.")
			return redirect("/index")
		else:
			messages.error(request,"Invalid username or password.")
	else:
		messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="login.html", context={"login_form":form})
'''
def login_request(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username = username, password = password)
        if user is not None :
            login(request, user)
            messages.success(request, f"You are now logged in as {username}")
            return redirect('index')
        else:
            messages.success(request, 'Error loggin in')
            return redirect('login')
    else:
        return render(request, 'login.html',{})

def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data['username']
			password = form.cleaned_data['password1']
			user = authenticate(username = username, password = password)
			login(request, user)
			messages.success(request, f'You have registered as {username} successfully..')
			return redirect('/index')
	else:
		form = NewUserForm()
	return render(request=request, template_name="register.html", context={"form":form})

def logout_request(request):
	logout(request)
	messages.info(request, "You have successfully logged out.") 
	return redirect("/login")

def search(request):
    if request.method == 'POST':
        searched = request.POST['searched']
        return render(request, 'search.html',{'searched':searched})
    else:
        return render(request, 'search.html')
    
