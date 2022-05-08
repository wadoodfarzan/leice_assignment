#Django Imports
from django.contrib.auth.models import User
from django_elasticsearch_dsl import Document, fields
from django_elasticsearch_dsl.registries import registry

#Our Custom Imports
from company.models import Company
@registry.register_document
class CompanyDocument(Document):
    class Index:
        name = 'companies' #name of search index
        settings = {
            'number_of_shards': 1,
            'number_of_replicas': 0,
        }

    class Django:
        model = Company #calling the model name
        fields = [
            'id',
            'name'
        ] #fields to be indexed