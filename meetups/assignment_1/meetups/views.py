import re
from django.shortcuts import render, get_object_or_404
import random
from .models import *
from .forms import *
from django.views.generic import CreateView
from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.contrib.sessions.models import Session
from django.urls import reverse
from django.utils import timezone
from datetime import timedelta
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import base64
import qrcode
from io import BytesIO
from django.views.decorators.csrf import csrf_protect

# these are for knowing which page to return for each link

def Index(request):
    return render(request, 'index.html')

@csrf_protect
class UserSignupView(CreateView):
    model = User
    form_class = UserSignupForm
    template_name = 'register.html'

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('create_meetup')

@csrf_protect
class UserLoginView(LoginView):
    template_name='login.html'

def logout_user(request):
    logout(request)
    return redirect("/")

@login_required
def make_pizza(request):
    user = request.user
    topping_fields = ['chicken', 'pepperoni', 'mushrooms', 'olives', 'ham', 'pineapple', 'onion', 'peppers']
    if request.method == 'POST':
        form = PizzaOrderForm(request.POST)
        if form.is_valid():
            PizzaOrder.objects.filter(user=user)

            pizza = form.save(commit=False)
            pizza.user = user
            pizza.delivery_datetime = timezone.now()
            pizza.save()
            request.session['pizzaid'] = pizza.id
            return redirect('payment_info')  # Redirect to success page
    else:
        form = PizzaOrderForm()
        return render(request, 'create_order.html', {'form': form})

@login_required
def payment_info(request):
    user = request.user
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            pizzaid = request.session.get('pizzaid')
            payment = form.save(commit=False)
            payment.save()
            address = payment.address
            request.session['address'] = address
            return redirect('success', pizzaid=pizzaid)
    else:
        form = PaymentForm()
    return render(request, 'payment_info.html', {'form': form})

def success(request, pizzaid):
    pizza = get_object_or_404(PizzaOrder, id=pizzaid)
    address = request.session.get('address')
    return render(request, 'success.html', {'pizza' :pizza, 'address': address})

def contact(request):
    return render(request, 'contact.html')

def about(request):
    return render(request, 'about.html')

def style(request):
    return render(request, 'style.css')

def location(request):
    return render(request, 'create_meetup.html')

def friends_list(request):
    return render(request, 'friends_list.html')

def history(request):
    return render(request, 'history.html')
