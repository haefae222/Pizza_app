# forms.py
from .models import *
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.forms import ModelForm, ModelChoiceField
from django.db import transaction

# these are our forms, for accounts and ordering pizzas etc
# and things like authentication.
# pizza form probably isnt needed, user form will probably
# have to be modified.

class UserSignupForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_admin = False
        user.email = self.cleaned_data['username']
        user.save()
        return user

class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)

class MeetupToDoForm(forms.ModelForm):
    class Meta:
        model = MeetupToDo
        fields = ['person_to_meet', 'meet_time']