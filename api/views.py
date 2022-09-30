from django.shortcuts import render
from rest_framework import generics, serializers, status
from api.serializers import *
from api.models import *
#from api.permissions import IsOwnerOrReadOnle

##################

class RestaurantAddView(generics.CreateAPIView):
    serializer_class = RestaurantSerializer
    #permission_classes = (IsOwnerOrReadOnle, )

class RestaurantListView(generics.ListAPIView):
    serializer_class = RestaurantSerializer
    queryset = Restaurant.objects.all()

##################

class EmployeeAddView(generics.CreateAPIView):
    serializer_class = EmployeeSerializer
    #permission_classes = (IsOwnerOrReadOnle,)

class EmployeeListView(generics.ListAPIView):
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()

#################

class MenuAddView(generics.CreateAPIView):
    serializer_class = MenuSerializer
    #permission_classes = (IsOwnerOrReadOnle,)

class MenuListView(generics.ListAPIView):
    serializer_class = MenuSerializer
    queryset = Menu.objects.all()

#################

class DishAddView(generics.CreateAPIView):
    serializer_class = DishSerializer
    #permission_classes = (IsOwnerOrReadOnle,)

class DishListView(generics.ListAPIView):
    serializer_class = DishSerializer
    queryset = Dish.objects.all()

#################

class Menu_RestaurantAddView(generics.CreateAPIView):
    serializer_class = Menu_RestaurantSerializer
    #permission_classes = (IsOwnerOrReadOnle,)

class Menu_RestaurantListView(generics.ListAPIView):
    serializer_class = Menu_RestaurantSerializer
    queryset = Menu_Restaurant.objects.all()

#################

class Menu_DishAddView(generics.CreateAPIView):
    serializer_class = Menu_DishSerializer
    #permission_classes = (IsOwnerOrReadOnle,)

class Menu_DishListView(generics.ListAPIView):
    serializer_class = Menu_DishSerializer
    queryset = Menu_Dish.objects.all()