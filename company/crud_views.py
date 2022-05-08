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
def show(request):  
    companies = Company.objects.all()  
    return render(request,"show.html",{'companies':companies})  
def edit(request, id):  
    company = Company.objects.get(id=id)  
    return render(request,'edit.html', {'company':company})  
def update(request, id):  
    company = Company.objects.get(id=id)  
    form = CompanyForm(request.POST, instance = company)  
    if form.is_valid():  
        form.save()  
        return redirect("/companies/show")  
    return render(request, 'edit.html', {'company': company})  
def destroy(request, id):  
    company = Company.objects.get(id=id)  
    company.delete()  
    return redirect("/companies/show")  