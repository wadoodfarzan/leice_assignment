from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import CompanySerializer
from company.models import Company
from rest_framework import viewsets
from elasticsearch_dsl import Q
from company.documents import CompanyDocument
class CompanyViewSet(APIView):

    # 1. List all
    def get(self, request, company_id=None):
        '''
        List all the todo items for given requested user
        '''
        
        serializer_context = {
            'request': request,
        }
        # queryset = Company.objects.filter(id=id).all()
        queryset = Company.objects.filter(id=company_id).prefetch_related('descendant_companies')
        serializer = CompanySerializer(queryset, many=True,context=serializer_context)
    
        return Response(serializer.data, status=status.HTTP_200_OK)


class CompanySearchViewSet(APIView):

    # 1. List all
    def get(self, request, user_id=None,search=None):
        '''
        List all the todo items for given requested user
        '''
        
        serializer_context = {
            'request': request,
        }

        q = Q('multi_match',query=search,fields=['name'])
        search = CompanyDocument.search().query(q)
        response = search.execute()
        print('responseresponseresponse',type(response))
        # print all the hits
        print('searchsearchsearch',search)
        result = []
        for hit in search:
            result.append({"comapny_name" : hit.name})
            print(hit.name)

        queryset = Company.objects.all()
        # queryset = Company.objects.filter(id=user_id).prefetch_related('descendant_companies')
        serializer = CompanySerializer(queryset, many=True,context=serializer_context)
    
        return Response(result, status=status.HTTP_200_OK)