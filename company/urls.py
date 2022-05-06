from django.urls import path, include
from company.views import CompanyViewSet, CompanySearchViewSet


urlpatterns = [
   path('descendant-companies/<int:company_id>/', CompanyViewSet.as_view()),
   path('search-companies/<int:user_id>/<str:search>', CompanySearchViewSet.as_view()),
   ]