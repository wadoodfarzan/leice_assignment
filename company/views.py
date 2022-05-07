from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import CompanySerializer
from company.models import Company, User
from rest_framework import viewsets
from elasticsearch_dsl import Q
from company.documents import CompanyDocument
import operator
from functools import reduce
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

        company = User.objects.filter(id=user_id).values('company_id')[0]
        print('parent_company',company['company_id'])
        
        # child_companies = Company.objects.filter(parent_id=company['company_id']).values('id')
        
        child_companies = get_nested_child(company['company_id'])
        print('RRRRRRRRRRRRRRRRRRRRRRRRRRRRRR',get_nested_child(company['company_id']))
        #get all the child companies of the parent
        
        
            
        
        print('child_companiesAAAAAAAAAAAAAAAAAAAAAAA',child_companies)
        # child_company_id_list = []
        # for id in list(child_companies):
        #     child_company_id_list.append(id['id'])
        
        # print('child_companies',child_company_id_list)
        queries = []
        q = Q(
                'multi_match',
                query=search,
                fields=['name'],
            )
        queries.append(q)
        
        child_queries = []
        if child_companies:
            for company_id in child_companies:
                child_queries.append(Q(
                'term',
                id=company_id,
                ))
        
        child_queries.append(Q(
                'match',
                id=company['company_id'],
                ))
        
        elastic_query = reduce(operator.iand, queries)
        elastic_filter = reduce(operator.ior, child_queries)
        print('queriesqueries',elastic_query)
        # print('queriesqueries',reduce(operator.iand, elastic_query))
        elastic_search = CompanyDocument.search().query(elastic_query).filter(elastic_filter)
        

        elastic_search.execute()
        
        # query = 'programming'
        # q = Q(
      	# 	'bool',
     	# 		must=[
        #  			Q('match', name=search),
     	# 			],
     	# 		# must_not=[
        #  		# 	Q('match', id='ruby'),
     	# 		# 		],
     	# 		should=[
        #  			Q('match', id=3),
     	# 			],
     	# 		minimum_should_match=1)
        # elastic_search = CompanyDocument.search().query(q)
        # elastic_search.execute()

        result = []
        for hit in elastic_search:
            result.append({
                "company_id" : hit.id,
                "company_name" : hit.name,
                "user_id" : user_id
                })
            print(hit.name)

    
        return Response(result, status=status.HTTP_200_OK)
    

def get_nested_child(company,child_companies=None):
    print('companycompanycompany------------1',company)
    # Company.objects.filter(parent_id=company['company_id']).values('id')
    if child_companies is None:
        child_companies = []

    company_id = Company.objects.filter(parent_id=company).values('id')
    print('company_idcompany_idcompany_id----------2',company_id)
    if company_id:
        for id in list(company_id):
            print('company_idcompany_idcompany_id----------3',id['id'])
            child_companies.append(id['id'])
            print('company_idcompany_idcompany_id----------3--1',child_companies)
            print('company_idcompany_idcompany_id----------4',company_id,'------',id)
            get_nested_child(id['id'],child_companies)
    else:
        pass
    
    return child_companies
             
    