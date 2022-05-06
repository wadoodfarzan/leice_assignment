from dataclasses import field
from rest_framework import serializers
from company.models import Company
class DescendantCompanies(serializers.ModelSerializer):

        # self.fields['descendant_companies'] = CompanySerializer()
    class Meta:
        model = Company
        fields = ('id', 'name','parent_id','descendant_companies')
        depth = 1
        

# descendant_companies = DescendantCompanies(many=True, read_only=True)
class CompanySerializer(serializers.ModelSerializer):
    # id = serializers.PrimaryKeyRelatedField()
    descendant_companies = DescendantCompanies(many=True, read_only=True)
    # print('descendant_companiesdescendant_companies',descendant_companies)
    class Meta:
        model = Company
        fields = ('id', 'name','parent_id', 'descendant_companies')
        # fields = "__all__"
