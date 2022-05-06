from django.urls import path, include
from company.views import CompanyViewSet


urlpatterns = [
   path('descendant-companies/<int:id>/', CompanyViewSet.as_view()),
   ]