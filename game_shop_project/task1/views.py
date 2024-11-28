from django.shortcuts import render, redirect
from .models import Buyer, Game
from .forms import UserRegister
from django.contrib.auth.hashers import make_password

def register_view(request):
    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            age = form.cleaned_data['age']
            password = form.cleaned_data['password']

            if not Buyer.objects.filter(name=name).exists():
                hashed_password = make_password(password)
                Buyer.objects.create(
                    name=name,
                    age=age,
                    password=hashed_password
                )
                return redirect('home')
            else:
                form.add_error('name', 'Пользователь с таким именем уже существует.')
    else:
        form = UserRegister()

    return render(request, 'registration_page.html', {'form': form})

def home_view(request):
    return render(request, 'home.html')

def shop_view(request):
    games = Game.objects.all()
    return render(request, 'shop.html', {'games': games})

def cart_view(request):
    return render(request, 'cart.html')

