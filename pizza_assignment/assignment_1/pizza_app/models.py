from email.policy import default
from django.db import models
from django.contrib.auth.models import AbstractUser

from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
#... any other imports

# this is for our actual classes, such as users and pizzas

class UserManager(BaseUserManager):
    """Define a model manager for User model with no username field."""

    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """Create and save a User with the given email and password."""
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        """Create and save a regular User with the given email and password."""
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)

class User(AbstractUser):
    email = models.EmailField('Email', unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = UserManager()

class pizza_crust(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return f"Crust: {self.name}"

class pizza_cheese(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return f"Cheese: {self.name}"

class pizza_sauce(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return f"Sauce: {self.name}"

class pizza_size(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return f"Size: {self.name}"

class PizzaOrder(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    delivery_datetime = models.DateTimeField(auto_now_add=True)
    pizza_crust = models.ForeignKey(pizza_crust, on_delete=models.CASCADE)
    pizza_cheese = models.ForeignKey(pizza_cheese, on_delete=models.CASCADE)
    pizza_sauce = models.ForeignKey(pizza_sauce, on_delete=models.CASCADE)
    pizza_size = models.ForeignKey(pizza_size, on_delete=models.CASCADE)
    olives = models.BooleanField(default=False)
    ham = models.BooleanField(default=False)
    pineapple = models.BooleanField(default=False)
    peppers = models.BooleanField(default=False)
    extra_cheese =models.BooleanField(default=False)
    mushrooms = models.BooleanField(default=False)
    pepperoni = models.BooleanField(default=False)
    chicken = models.BooleanField(default=False)

    def __str__(self):
        return f"Pizza Order {self.id}"

class payment(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    card_number = models.CharField(max_length=12)
    card_date = models.CharField(max_length=4)
    cvv = models.CharField(max_length=3)