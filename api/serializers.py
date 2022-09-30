from rest_framework import serializers
from api.models import *

class RestaurantSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Restaurant
        #fields = ('restaurant_name',)
        fields = '__all__'

class EmployeeSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Employee
        #fields = ('employee_name','employee_surname','restaurant_name')
        fields = '__all__'

class DishSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Dish
        #fields = ('dish_name',)
        fields = '__all__'

class MenuSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Menu
        #fields = ('menu_name',)
        fields = '__all__'


class Menu_RestaurantSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Menu_Restaurant
        fields = '__all__'

class Menu_DishSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Menu_Dish
        fields = '__all__'
