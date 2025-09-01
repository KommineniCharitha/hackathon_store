from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  # redirect to homepage
    else:
        form = UserCreationForm()
    return render(request, "store/signup.html", {"form": form})


from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import render, redirect

def signup_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # auto login after signup
            return redirect('home')  # redirect to homepage
    else:
        form = UserCreationForm()
    return render(request, 'store/signup.html', {'form': form})



from django.contrib.auth.forms import AuthenticationForm

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'store/login.html', {'form': form})



def logout_view(request):
    logout(request)
    return redirect('home')


from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

def signup_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # log in the new user automatically
            return redirect('product_list')  # redirect to home after signup
    else:
        form = UserCreationForm()
    return render(request, 'store/signup.html', {'form': form})

from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello, your site is working!")
