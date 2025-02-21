# forms.py
from .models import *
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.forms import ModelForm, ModelChoiceField
from django.db import transaction


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


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["text", "image"]

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['content']  

  # cleaning the content making sure it's valid and not empty 
    def clean_content(self):
        content = self.cleaned_data['content']
        if len(content) < 1:
            raise forms.ValidationError("Message cannot be empty.")
        return content
