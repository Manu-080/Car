from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
# Create your models here.


class Customer(models.Model):
    user = models.OneToOneField(User, verbose_name=_("user"), on_delete=models.CASCADE)
    phone = models.CharField(max_length=20,unique=True)
    
    

    def __str__(self) -> str:
        return self.user.username