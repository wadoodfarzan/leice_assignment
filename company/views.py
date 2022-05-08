#Django Rest Imports
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

#Python Imports
import operator
from functools import reduce

#Elastic Search Import
from elasticsearch_dsl import Q

#Our Custom Imports
from company.documents import CompanyDocument
from company.models import Company, User
from company.serializers import CompanySerializer

class CompanyViewSet(APIView):

    """Creates company object combining different elements from the list. And insert record in Database.
    :param self: self
    :param request: django request object
    :param company_id: int
    :return: Json Response
    """
    def get(self, request, company_id=None):
        serializer_context = {'request': request,}
        queryset = Company.objects.filter(id=company_id).prefetch_related('descendant_companies') #querying database for required dataset
        serializer = CompanySerializer(queryset, many=True,context=serializer_context) #calling company serializer
    
        return Response(serializer.data, status=status.HTTP_200_OK)

class CompanySearchViewSet(APIView):

    """Creates company object combining different elements from the list. And insert record in Database.
    :param self: self
    :param request: django request object
    :param user_id: int
    :param search: string
    :return: Json Response
    """
    def get(self, request, user_id=None,search=None):
        company = get_user_company(user_id) #calling get_user_company function
        child_company_ids = get_nested_child(company['company_id']) #calling get_nested_child function    
        elastic_search = create_elastic_search_query(company,child_company_ids,search).execute() #calling create_elastic_search_query function and execute query
        response = create_elastic_response(elastic_search,user_id) #calling create_elastic_response function

        return Response(response, status=status.HTTP_200_OK)
    
"""Return User Company
:param user_id: int
:return: dictionary
"""
def get_user_company(user_id): 
    return User.objects.filter(id=user_id).values('company_id')[0] #querying company assigned to user

"""Loop Through Companies Table and find all the child of the parent Company Resursively.
:param company: int
:param child_companies: list
:return: list
"""
def get_nested_child(company,child_companies=None):
    if child_companies is None:
        child_companies = []
    company_id = Company.objects.filter(parent_id=company).values('id')#getting primary keys of childs against parent
    if company_id:
        for id in list(company_id): #looping through the childs
            child_companies.append(id['id'])
            get_nested_child(id['id'],child_companies) #Calling the get_nested_child in resursion
    else:
        pass
    
    return child_companies

"""Create Elastic Search Query on the basis of search text and company ids
:param company: int
:param child_companies: list
:param search: string
:return: elastic search object
"""
def create_elastic_search_query(company,child_company_ids,search):
    company_name = []
    q = Q('multi_match',query=search,fields=['name'],) #search string match query
    company_name.append(q)     
    company_ids = []
    if child_company_ids:
        for company_id in child_company_ids:
            company_ids.append(Q('term',id=company_id,)) #company ids filter query
        
    company_ids.append(Q('match',id=company['company_id'],))    
    query = reduce(operator.iand, company_name) #search string match
    filter = reduce(operator.ior, company_ids) #company ids filter
    """Equal Mysql Query
    SELECT * FROM company_company WHERE name LIKE '%AB%' AND id IN (3,4,5);
    """
    return CompanyDocument.search().query(query).filter(filter)

"""Return Custom list by reponse from elastic search
:param elastic_search: dictionary of elastic search type
:param user_id: int
:return: list
"""
def create_elastic_response(elastic_search,user_id):
    response = []
    if elastic_search:
        for result in elastic_search: #loop through response
            response.append({"company_id" : result.id,"company_name" : result.name,"user_id" : user_id}) #making list through elastic search response
        
    return response