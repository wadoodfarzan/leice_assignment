from django.urls import path
from company import views, crud_views

urlpatterns = [
   path('descendant-companies/<int:company_id>/', views.CompanyViewSet.as_view()),
   path('search-companies/<int:user_id>/<str:search>', views.CompanySearchViewSet.as_view()),
   path('show',crud_views.show),  
   ]