from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.timezone import now
import datetime


# Create your models here.
class User(AbstractUser):
    pass

    def __str__(self):
        return f"{self.username}"

class Wallet(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    pub_key = models.CharField(max_length = 64)
    priv_key = models.CharField(max_length = 64)
    balance = models.PositiveIntegerField(default = 0)

    def __str__(self):
        return f"Wallet of {self.owner.username}."
        
