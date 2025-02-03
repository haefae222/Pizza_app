from django.urls import path
from . import views
from .forms import *

# these connect the links to each page,
# dont forget to add each one to view.py
# and make sure the links in the templates are right too

urlpatterns = [
   path('', views.Index, name="Index"),
   path('create_order/', views.make_pizza, name="create_order"),
   path('register/', views.UserSignupView.as_view(), name="register"),
   path('login/',views.LoginView.as_view(template_name="login.html", authentication_form=UserLoginForm)),
   path('logout/', views.logout_user, name="logout"),
   path('create_order/payment_info', views.payment_info, name="payment_info"),
   path('create_order/payment/success<int:pizzaid>/', views.success, name="success"),
   path('orders/', views.orders, name="orders"),
   path('contact/', views.contact, name="contact"),
   path('about/', views.about, name="about"),
]