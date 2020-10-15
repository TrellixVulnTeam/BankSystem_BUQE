from django.db import models

from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles
# Create your models here.

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted([(item, item) for item in get_all_styles()])


class Bank(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=100, blank=True)

    class Meta:
        ordering = ['name']

class Customer(models.Model):
    name_customer = models.CharField(max_length=200)
    debit = models.IntegerField()
    credit = models.CharField(max_length=200)

    class Meta:
        ordering = ['name_customer']