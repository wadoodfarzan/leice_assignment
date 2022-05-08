#Django Imports
from rest_framework import serializers

#Our Custom Imports
from company.models import Company

"""Company Descendant Serializer for Serializing the Child Companies"""     
class DescendantCompanies(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ('id', 'name','parent_id','descendant_companies')
        depth = 1
"""Company Serializer for Serializing the Company Object"""        
class CompanySerializer(serializers.ModelSerializer):
    
    descendant_companies = DescendantCompanies(many=True, read_only=True)
    class Meta:
        model = Company
        fields = ('id', 'name','parent_id', 'descendant_companies')