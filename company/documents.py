from django.contrib.auth.models import User
from django_elasticsearch_dsl import Document, fields
from django_elasticsearch_dsl.registries import registry

from company.models import Company


@registry.register_document
class CompanyDocument(Document):
    id = fields.IntegerField()

    class Index:
        name = 'companies'
        settings = {
            'number_of_shards': 1,
            'number_of_replicas': 0,
        }

    class Django:
        model = Company
        fields = [
            'name',
        ]