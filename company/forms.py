#Django Imports
from django import forms  

#Our Custom Imports
from company.models import Company  
class CompanyForm(forms.ModelForm):  
    class Meta:  
        model = Company  
        fields = "__all__"  