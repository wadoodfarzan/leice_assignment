from django import forms  
from company.models import Company  
class EmployeeForm(forms.ModelForm):  
    class Meta:  
        model = Company  
        fields = "__all__"  