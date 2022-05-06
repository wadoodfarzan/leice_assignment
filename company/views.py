from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import CompanySerializer
from company.models import Company
from rest_framework import viewsets
class CompanyViewSet(APIView):

    # 1. List all
    def get(self, request, id=None):
        '''
        List all the todo items for given requested user
        '''
        
        serializer_context = {
            'request': request,
        }
        queryset = Company.objects.filter(id=id).all()
        
        serializer = CompanySerializer(queryset, many=True,context=serializer_context)
    
        return Response(serializer.data, status=status.HTTP_200_OK)

        
        
        queryset = Company.objects.all() 
        serializer = CompanySerializer(queryset,many=True, context=serializer_context)
        return Response(serializer.data, status=status.HTTP_200_OK)