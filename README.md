# Leica Geosystems Assignment
## _Implementation of Elastic Search In Django Restful with CRUD_

Django Elastic Search Implementation with ACL.

Phthon, Django, Django Rest Framework, HTML, CSS Mysql.

## Requirements

Package                  Version  
------------------------ ---------
- asgiref                  3.5.1    
- backports.zoneinfo       0.2.1    
- certifi                  2021.10.8
- Django                   4.0.4    
- django-elasticsearch-dsl 7.2.2    
- djangorestframework      3.13.1   
- elastic-transport        8.1.2    
- elasticsearch            7.17.3   
- elasticsearch-dsl        7.4.0    
- mysqlclient              2.1.0    
- pip                      20.0.2   
- pkg-resources            0.0.0    
- python-dateutil          2.8.2    
- pytz                     2022.1   
- setuptools               44.0.0   
- six                      1.16.0   
- sqlparse                 0.4.2    
- urllib3                  1.26.9 

## Features

- ACL
- CRUD
- Elastic Search

And of course Assignment itself is open source with a [public repository](https://github.com/wadoodfarzan/leice_assignment) on GitHub.

## Installation

Install the dependencies and devDependencies and start the server.

```sh
python --version
```
`
Python 3.8.10
`
```sh
python3 -m venv venv (if error sudo apt install python3.8-venv)
```

```sh
source venv/bin/activate
```
`
venv
`
```sh
pip install django
```
`
Collecting django
  Downloading Django-4.0.4-py3-none-any.whl (8.0 MB)
     |████████████████████████████████| 8.0 MB 2.3 MB/s 
Collecting sqlparse>=0.2.2
  Downloading sqlparse-0.4.2-py3-none-any.whl (42 kB)
     |████████████████████████████████| 42 kB 333 kB/s 
Collecting asgiref<4,>=3.4.1
  Downloading asgiref-3.5.1-py3-none-any.whl (22 kB)
Collecting backports.zoneinfo; python_version < "3.9"
  Downloading backports.zoneinfo-0.2.1-cp38-cp38-manylinux1_x86_64.whl (74 kB)
     |████████████████████████████████| 74 kB 1.1 MB/s 
Installing collected packages: sqlparse, asgiref, backports.zoneinfo, django
Successfully installed asgiref-3.5.1 backports.zoneinfo-0.2.1 django-4.0.4 sqlparse-0.4.2
`
```sh
django-admin startproject leica_assignment .
```
```sh
python manage.py runserver
```
`
Watching for file changes with StatReloader
Performing system checks...
System check identified no issues (0 silenced).
You have 18 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
Run 'python manage.py migrate' to apply them.
May 04, 2022 - 13:00:08
Django version 4.0.4, using settings 'leica_assignment.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
`
```sh
pip list
```
`
Package            Version
asgiref            3.5.1  
backports.zoneinfo 0.2.1  
Django             4.0.4  
pip                20.0.2 
pkg-resources      0.0.0  
setuptools         44.0.0 
sqlparse           0.4.2 
`
```sh
pip install -r requirements.txt
```

```sh
python manage.py makemigrations company
```
`
    company/migrations/0001_initial.py
    - Create model User
    - Create model Company
    - Add field comapny to user
    - Add field groups to user
    - Add field user_permissions to user
`
```sh
python manage.py migrate
```
`
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, sessions
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying admin.0003_logentry_add_action_flag_choices... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying auth.0008_alter_user_username_max_length... OK
  Applying auth.0009_alter_user_last_name_max_length... OK
  Applying auth.0010_alter_group_name_max_length... OK
  Applying auth.0011_update_proxy_permissions... OK
  Applying auth.0012_alter_user_first_name_max_length... OK
  Applying sessions.0001_initial... OK
`
```sh
python manage.py createsuperuser --username=leica --email=leica@company.com
```
`
password leica
`
```sh
pip install djangorestframework
```
```sh
sudo apt-get install elasticsearch=7.10.1
sudo systemctl start elasticsearch
curl http://localhost:9200/

```
`
--2022-05-06 22:53:45--  https://artifacts.elastic.co/downloads/elasticsearch/elasticsearch-8.2.0-linux-x86_64.tar.gz
Resolving artifacts.elastic.co (artifacts.elastic.co)... 34.120.127.130, 2600:1901:0:1d7::
Connecting to artifacts.elastic.co (artifacts.elastic.co)|34.120.127.130|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 529729465 (505M) [application/x-gzip]
Saving to: ‘elasticsearch-8.2.0-linux-x86_64.tar.gz’
elasticsearch-8.2.0-linux-x86_64.tar.gz             100%[================================================================================================================>] 505.19M  3.50MB/s    in 1m 59s  
2022-05-06 22:55:45 (4.23 MB/s) - ‘elasticsearch-8.2.0-linux-x86_64.tar.gz’ saved [529729465/529729465]
`
```sh
python manage.py search_index --rebuild
```
`
Are you sure you want to delete the 'companies' indexes? [y/N]: y
Deleting index 'companies'
Creating index 'companies'
Indexing 5 'Company' objects 
`

## Links
- https://docs.djangoproject.com/en/4.0/intro/tutorial01/
- https://www.digitalocean.com/community/tutorials/how-to-use-postgresql-with-your-django-application-on-ubuntu-20-04
- https://docs.djangoproject.com/en/4.0/howto/custom-management-commands/
- https://stackoverflow.com/questions/51577441/how-to-seed-django-project-insert-a-bunch-of-data-into-the-project-for-initi
- https://www.ginkgobioworks.com/2021/02/04/creating-a-rest-api-using-django-rest-framework/
- https://blog.logrocket.com/django-rest-framework-create-api/
- https://stackoverflow.com/questions/58779929/django-url-to-specific-request-method
- https://testdriven.io/blog/django-drf-elasticsearch/
- https://djangotricks.blogspot.com/2018/06/data-filtering-in-a-django-website-using-elasticsearch.html


