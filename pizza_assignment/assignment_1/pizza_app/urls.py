from django.urls import path
from . import views
from .forms import *

# these connect the links to each page,
# dont forget to add each one to view.py
# and make sure the links in the templates are right too

urlpatterns = [
   path('', views.Index, name="Index"),
   path('register/', views.UserSignupView.as_view(), name="register"),
   path('login/',views.LoginView.as_view(template_name="login.html", authentication_form=UserLoginForm)),
   path('logout/', views.logout_user, name="logout"),
   path('contact/', views.contact, name="contact"),
   path('about/', views.about, name="about"),
   path('style/', views.style, name="style"),
]