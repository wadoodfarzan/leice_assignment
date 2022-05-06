from rest_framework import serializers
from company.models import Company

class CompanySerializer(serializers.HyperlinkedModelSerializer):
   class Meta:
       model = Company
       fields = ('id','name','parent_id')