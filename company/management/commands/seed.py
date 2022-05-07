# <project>/<app>/commands/seed.py
from django.core.management.base import BaseCommand
from datetime import datetime
from django.utils.timezone import make_aware
from django.db import connection
from django.contrib.auth.hashers import make_password


import random
import hashlib

from company.models import Company
from company.models import User

# python manage.py seed --mode

class Command(BaseCommand):
    help = "seed database for testing and development."

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        self.stdout.write('Seeding data...')
        run_seed()
        self.stdout.write(self.style.SUCCESS('Successfully seeded data'))
        

# def make_password(password):
#     """Generates the hash for a password."""
#     assert password
#     hash = hashlib.md5(password.encode('utf-8')).hexdigest()
#     return hash


def create_companies(i):
    """Creates an company object combining different elements from the list"""
    
    company_name = ["Leica AB", "HexaGon AB", "Park Street", "MG Road", "Indiranagar"]

    company = Company(
        name=company_name[i-1],
        parent_id=random.randint(1,5),
        # parent_id=1,
    )
    company.save()
    print(Company.objects.all())
    return company

def create_users(i):
    """Creates an company object combining different elements from the list"""
    
    user_name = ["LeicaUser", "HexaGonUser", "ParkStreetUser", "MGRoadUser", "IndiranagarUser"]
    first_name = ["Leica User", "HexaGon User", "Park Street User", "MG Road User", "Indiranagar User"]
    last_name = ["Last Leica User", "Laste HexaGon User", "Laste Park Street User", "Laste MG Road User", "Laste Indiranagar User"]
    email = ["LastLeicaUser@abc.com", "LasteHexaGonUser@abc.com", "LasteParkStreetUser@abc.com", "LasteMGRoadUser@abc.com", "LasteIndiranagarUser@abc.com"]
    naive_datetime = datetime.now()
    
    user = User(
        password=make_password('hello123'),
        is_superuser=0,
        username=user_name[i-1],
        first_name=first_name[i-1],
        last_name=last_name[i-1],
        email=email[i-1],
        is_staff=0,
        is_active=1,
        date_joined=make_aware(naive_datetime),
        company_id=random.randint(1,5)
    )
    user.save()
    print(Company.objects.all())
    return user

def run_seed():
    """ Seed database based on mode

    :param mode: refresh / clear 
    :return:
    """
    with connection.constraint_checks_disabled():
        # Creating 5 companyes
        for i in range(1,6):
            create_companies(i)
        
        # Creating 5 companyes
        for i in range(1,6):
            create_users(i)
