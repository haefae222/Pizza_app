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

class PizzaOrderForm(forms.ModelForm):
      class Meta:
        model = PizzaOrder
        fields = [ 'pizza_crust', 'pizza_cheese', 'pizza_sauce', 'pizza_size', 'chicken', 'pepperoni', 'ham', 'pineapple', 'mushrooms', 'olives', 'peppers']  

        def __init__(self, *args, **kwargs):
            super(PizzaOrderForm, self).__init__(*args, **kwargs)
            self.fields['size'].queryset = pizza_size.objects.all()
            self.fields['cheese'].queryset = pizza_cheese.objects.all()
            self.fields['sauce'].queryset = pizza_sauce.objects.all()
            self.fields['crust'].queryset = pizza_crust.objects.all()

        def clean(self):
            cleaned_data = super().clean()
            for field_name in ['size', 'cheese', 'sauce', 'crust']:
                field_value = cleaned_data.get(field_name)
                if '-' in str(field_value):
                    raise forms.ValidationError("Please fill out all fields")
            return cleaned_data

class PaymentForm(forms.ModelForm):
    class Meta:
        model = payment
        fields = ['name', 'address', 'card_number', 'card_date', 'cvv' ]

        def clean_card_number(self):
            cleaned_data = super().clean
            card_number = self.cleaned_data['card_number']
            if len(card_number) != 16 or not card_number.isdigit():
                raise forms.ValidationError("Please provide a valid 16-digit card number")
            
        def clean_card_date(self):
            card_date = self.clean_card_date['card_date']
            if len(card_date) != 4 or not card_date.isdigit():
                raise forms.ValidationError("Invalid card expiration date format. Use MMYY")
        
        def clean_card_cvv(self):
            card_cvv = self.clean_card_cvv['card_cvv']
            if len(card_cvv) != 3 or not card_cvv.isdigit():
                raise forms.ValidationError("CVV must be a 3-digit number")
                 
        name = models.CharField()
        address = models.CharField()
        card_number = models.CharField()
        card_date = models.CharField()
        cvv = models.CharField()