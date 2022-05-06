# from rest_framework import serializers
# from company.models import Company

# class CompanySerializer(serializers.HyperlinkedModelSerializer):
#     # parentCompany = serializers.PrimaryKeyRelatedField()
#     # descendant_companies = serializers.DescendantCompaniesSerializer()
#     descendant_companies = serializers.SerializerMethodField()
#     class Meta:
#        model = Company
#        fields = ('id','name','parent_id','descendant_companies',)
       
#     def get_descendant_companies(self, obj):
#         # queryset = Company.objects.filter(id=3).all()
#         # print(queryset)
#         return [{'assa':5,'assaas':6}]
#         # return JsonResponse(Company.objects.filter(id=3).all(),safe=False)
        


from rest_framework import serializers
from company.models import Company

class DescendantCompanies(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ('id', 'name','parent_id')

class CompanySerializer(serializers.ModelSerializer):
    # id = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    descendant_companies = DescendantCompanies(many=True, read_only=True)
    # print('descendant_companiesdescendant_companies',descendant_companies)
    class Meta:
        model = Company
        fields = ('id', 'name', 'parent_id', 'descendant_companies')
        # fields = "__all__"