# Generated by Django 3.2.12 on 2024-02-20 09:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pizza_app', '0004_payment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payment',
            name='PizzaOrder',
        ),
    ]
