from django.http import HttpResponse

from django.shortcuts import render, redirect, get_object_or_404

def home(request):
    return HttpResponse("Hello, welcome to the Store App 🎉")
from django.http import HttpResponse
from django.shortcuts import render
from .models import Product

def home(request):
    products = Product.objects.all()
    return render(request, 'store/home.html', {'products': products})


from django.contrib.auth.decorators import login_required
from .models import Product, Cart

@login_required
def add_to_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    cart_item, created = Cart.objects.get_or_create(user=request.user, product=product)
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    return redirect('cart')

@login_required
def cart_view(request):
    cart_items = Cart.objects.filter(user=request.user)
    return render(request, 'store/cart.html', {'cart_items': cart_items})


from django.shortcuts import render
from .models import Product

def product_list(request):
    products = Product.objects.all()   # get all products from DB
    return render(request, 'store/product_list.html', {'products': products})

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


from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('product_list')  # redirect to homepage after login
    else:
        form = AuthenticationForm()
    return render(request, 'store/login.html', {'form': form})


from django.contrib.auth import logout

def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect('product_list')


