from django.contrib import admin
from django.urls import path, include
from api.views import *

urlpatterns = [
    #path('api/v1/', include('api.urls')),
    path('restaurant/add/', RestaurantAddView.as_view()),
    path('restaurant/list/', RestaurantListView.as_view()),
    path('employee/add/', EmployeeAddView.as_view()),
    path('employee/list/', EmployeeListView.as_view()),
    path('menu/add/', MenuAddView.as_view()),
    path('menu/list/', MenuListView.as_view()),
    path('dish/add/', DishAddView.as_view()),
    path('dish/list/', DishListView.as_view()),
    path('menu-restaurant/add/', Menu_RestaurantAddView.as_view()),
    path('menu-restaurant/list/', Menu_RestaurantListView.as_view()),
    path('menu-dish/add/', Menu_DishAddView.as_view()),
    path('menu-dish/list/', Menu_DishListView.as_view()),
]
