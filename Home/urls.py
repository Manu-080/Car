from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('details/<int:pk>',views.car_details,name='details'),
    path('list/<int:pk>',views.brand_list,name='brand_list'),
    path('comparison/',views.car_comparison,name='comparison'),
    path('search_car/',views.search_car,name='search-car'),
    
]
