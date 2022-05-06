from django.db import models
from django.conf import settings 
from django.contrib.auth.models import AbstractUser

class Company(models.Model):
    name = models.CharField(max_length=256,null=True, blank=True)
    parent = models.ForeignKey("self", on_delete=models.CASCADE, null=True, blank=True,related_name='descendant_companies')
    # user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    
    def __str__(self):
        return f"Company ID: {self.id} Name: {self.name}"


class User(AbstractUser):
    comapny = models.ForeignKey(Company, on_delete=models.SET_NULL, null=True, blank=True)