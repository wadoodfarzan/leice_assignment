#Django Imports
from django.core.management.base import BaseCommand
from django.utils.timezone import make_aware
from django.db import connection
from django.contrib.auth.hashers import make_password

#Python Imports
from datetime import datetime
import random

#Our Custom Imports
from company.models import Company
from company.models import User

# python manage.py seed

class Command(BaseCommand):
    help = "Seed Database for testing and development."
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        self.stdout.write('Seeding data...')
        run_seed()
        self.stdout.write(self.style.SUCCESS('Successfully seeded data'))

"""Creates company object combining different elements from the list. And insert record in Database.
:param row_id: loop index
:return:
"""
def create_companies(row_id):
    #5 company name lists
    company_name = ["Leica AB", "HexaGon AB", "Lime AB", "Nord Cloud Ab", "Microsoft PVT"]
    #calling company model and save record
    company = Company(
        name=company_name[row_id-1],
        parent_id=None if row_id == 1 else row_id-1, #First Company is not child of any company in order to stop infinite recursion
    )
    company.save()

    return True

"""Creates user object combining different elements from the list. And insert record in Database.
:param mode: row_id index
:return:
"""
def create_users(row_id):
    #lists with data to be inserted in User Table
    user_name = ["leica", "hexagon", "lime", "nordcloud", "microsoft"]
    first_name = ["Leica", "HexaGon", "Lime", "Nord Cloud", "Microsoft"]
    last_name = ["AB", "AB", "AB", "AB", "PVT"]
    email = ["Leica@Leica.com", "HexaGon@HexaGon.com", "Lime@Lime.com", "Nord@Cloud.com", "Microsoft@Microsoft.com"]
    #calling user model and save record
    user = User(
        password=make_password('123456'),
        is_superuser=0,
        username=user_name[row_id-1],
        first_name=first_name[row_id-1],
        last_name=last_name[row_id-1],
        email=email[row_id-1],
        is_staff=1,
        is_active=1,
        date_joined=make_aware(datetime.now()),
        company_id=random.randint(1,5)
    )
    user.save()
    return True

"""Call user and company seeder functions
:param:
:return: boolean
"""
def run_seed():
    with connection.constraint_checks_disabled():
        # Creating 5 companies
        for i in range(1,6):
            create_companies(i) #calling function
        
        # Creating 5 users
        for i in range(1,6):
            create_users(i) #calling function
        
    return True
