from django.db import models

# Create your models here.

class Payments(models.Model):
    user_name = models.CharField(max_length=255)
    amount_money = models.IntegerField()