#Django Rest Imports
from django.shortcuts import render

#Python Imports
import operator
from functools import reduce

#Elastic Search Import
from elasticsearch_dsl import Q

#Our Custom Imports
from company.models import Company, User

def show(request):  
    companies = Company.objects.all()  
    return render(request,"show.html",{'companies':companies})  