from django.db import models
from django.core.exceptions import ValidationError
import re


# Перевірка валідності номера телефону
def validate_phone(value):
    if not re.match(r'^\+\d{12}$', value):
        raise ValidationError(message=f'{value} is not a valid phone number')


class Provider(models.Model):
    name = models.CharField(max_length=255)
    contact_person = models.CharField(max_length=255)
    phone = models.CharField(max_length=255, validators=[validate_phone])
    account = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Material(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()

    def __str__(self):
        return self.name


class Supply(models.Model):
    date = models.DateField()
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE)
    material = models.ForeignKey(Material, on_delete=models.CASCADE)
    days = models.IntegerField()
    amount = models.IntegerField()

    def str(self):
        return f"Supply {self.id}"

    # Перевірка валідності днів


def validate_days(self):
    if not (0 < self.days < 8):
        raise ValidationError('Days must be between 1 and 7.')
