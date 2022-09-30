from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()


class Restaurant(models.Model):
    #restaurant_id = models.AutoField(primary_key=True)
    restaurant_name = models.CharField(max_length=80,primary_key=True,unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Employee(models.Model):
    #employee_id = models.AutoField(primary_key=True)
    employee_name = models.CharField(max_length=80)
    employee_surname = models.CharField(max_length=80)
    restaurant_name = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Menu(models.Model):
    #menu_id = models.AutoField(primary_key=True)
    menu_name = models.CharField(max_length=80,primary_key=True,unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Dish(models.Model):
    #dish_id = models.AutoField(primary_key=True)
    dish_name = models.CharField(max_length=80,primary_key=True,unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)



class Menu_Restaurant(models.Model):
    menu_name = models.ForeignKey(Menu, on_delete=models.CASCADE)
    menu_date = models.DateField()
    restaurant_name = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Menu_Dish(models.Model):
    menu_name = models.ForeignKey(Menu, on_delete=models.CASCADE)
    #menu_name = models.ForeignObject(Menu, on_delete=models.CASCADE)
    dish_name = models.ForeignKey(Dish, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    #dish_name = models.ForeignKey(Dish, on_delete=models.CASCADE)



