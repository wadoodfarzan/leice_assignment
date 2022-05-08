#Django Rest Imports
from django.shortcuts import render,redirect

#Python Imports
import operator
from functools import reduce

#Elastic Search Import
from elasticsearch_dsl import Q

#Our Custom Imports
from company.models import Company, User
from company.forms import CompanyForm  

"""Return Custom list by reponse from elastic search
:param request: django request object
:return: html redered
"""
def company(request):  
    if request.method == "POST":  
        form = CompanyForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/companies/show')  
            except:  
                pass  
    else:  
        form = CompanyForm()  
    return render(request,'index.html',{'form':form})  

"""Return Custom list by reponse from elastic search
:param request: django request object
:return: html redered
"""
def show(request):  
    companies = Company.objects.all()  
    return render(request,"show.html",{'companies':companies}) 
 
"""Return Custom list by reponse from elastic search
:param request: django request object
:param id: int
:return: html redered
"""
def edit(request, id):  
    company = Company.objects.get(id=id)  
    return render(request,'edit.html', {'company':company})  

"""Return Custom list by reponse from elastic search
:param request: django request object
:param id: int
:return: html redered
"""
def update(request, id):  
    company = Company.objects.get(id=id)  
    form = CompanyForm(request.POST, instance = company)  
    if form.is_valid():  
        form.save()  
        return redirect("/companies/show")  
    return render(request, 'edit.html', {'company': company})  

"""Return Custom list by reponse from elastic search
:param request: django request object
:param id: int
:return: html redered
"""
def destroy(request, id):  
    company = Company.objects.get(id=id)  
    company.delete()  
    return redirect("/companies/show")  