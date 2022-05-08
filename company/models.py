#Django Imports
from django.db import models
# from django.conf import settings 
from django.contrib.auth.models import AbstractUser

class Company(models.Model):
    #Defining Column Names for Company Table
    name = models.CharField(max_length=256,null=True, blank=True)
    parent = models.ForeignKey("self", on_delete=models.CASCADE, null=True, blank=True,related_name='descendant_companies')
    # user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    
    class Meta:
        verbose_name_plural = 'companies'
    def __str__(self):
        return f"{self.id}-{self.name}"

class User(AbstractUser):
    #Adding Company ID Foreign Key in User Table
    company = models.ForeignKey(Company, on_delete=models.SET_NULL, null=True, blank=True)