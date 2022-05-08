from django.urls import path
from django.contrib import admin  

from company import views, crud_views

urlpatterns = [
   path('descendant-companies/<int:company_id>', views.CompanyViewSet.as_view()),
   path('search-companies/<int:user_id>/<str:search>', views.CompanySearchViewSet.as_view()),
   
   path('admin', admin.site.urls),  
   path('company', crud_views.company),  
   path('show',crud_views.show),
   path('edit/<int:id>', crud_views.edit),  
   path('update/<int:id>', crud_views.update),  
   path('delete/<int:id>', crud_views.destroy),  
   ]