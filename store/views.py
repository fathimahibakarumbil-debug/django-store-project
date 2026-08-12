from django import forms
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Product
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required

class CustomUserCreationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.help_text = None

def register_view(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save() 
            messages.success(request, "Registration successful! Please login.")
          
            return redirect('login') 
        else:
            
            messages.error(request, "Registration failed. Username might already exist.")
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})

# Login View
def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
        else:
            messages.error(request, "Invalid username or password.")
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

# Logout View
def logout_view(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
# Home Page
def home(request):
    products = Product.objects.all()
    return render(request, 'home.html', {'products': products})


@login_required(login_url='login')
# Product List Page
def product_list(request):
    products = Product.objects.all()

    if request.method == 'POST' and request.POST.get('action') == 'save_product':
        pk = request.POST.get('product_id')
        product = get_object_or_404(Product, pk=pk)
        product.is_saved = True
        product.save()
        return redirect('saved_products')

    return render(request, 'products/product_list.html', {'products': products})


@login_required(login_url='login')
# Saved Products Page
def saved_products(request):
    products = Product.objects.filter(is_saved=True)
    return render(request, 'products/saved_products.html', {'products': products})


@login_required(login_url='login')
# Add Product
def add_product(request):
    if request.method == 'POST':
        price = request.POST.get('price')
        image_url = request.POST.get('image_url')

        if price:
            Product.objects.create(
                price=price,
                image_url=image_url,
                is_saved=False
            )
            return redirect('product_list')
        else:
            return render(request, 'products/add_product.html', {
                'error': 'Price is required.'
            })

    return render(request, 'products/add_product.html')


@login_required(login_url='login')
# Edit Product
def edit_product(request, pk):
    product = get_object_or_404(Product, pk=pk)

    if request.method == 'POST':
        price = request.POST.get('price')
        image_url = request.POST.get('image_url')

        if price:
            product.price = price
            product.image_url = image_url
            product.save()
            return redirect('product_list')
        else:
            return render(request, 'products/edit_product.html', {
                'product': product,
                'error': 'Price is required.'
            })

    return render(request, 'products/edit_product.html', {'product': product})


@login_required(login_url='login')
# Delete Product
def delete_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    product.delete()
    return redirect('product_list')


@login_required(login_url='login')
# Remove from Saved
def remove_saved_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    product.is_saved = False
    product.save()
    return redirect('saved_products')


@login_required(login_url='login')
# About Page
def about(request):
    return render(request, 'about.html')


@login_required(login_url='login')
# Contact Page
def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        messages.success(request, 'Your message has been sent successfully!')
        return redirect('contact')

    return render(request, 'contact.html')
















