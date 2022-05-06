from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import CompanySerializer
from company.models import Company
class CompanyViewSet(APIView):

    # 1. List all
    def get(self, request, id=None):
        '''
        List all the todo items for given requested user
        '''
        
        print(111111111111111111111111111,id)
        # todos = Todo.objects.filter(user = request.user.id)
        # serializer = TodoSerializer(todos, many=True)
        serializer_context = {
            'request': request,
        }
        queryset = Company.objects.all() 
        serializer = CompanySerializer(queryset,many=True, context=serializer_context)
        return Response(serializer.data, status=status.HTTP_200_OK)