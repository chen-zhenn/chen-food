from rest_framework import serializers
from foodmenu.models import Category, Culinary, Ingredient, Dish

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "name"]

class CulinarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Culinary
        fields = ["id", "name"]

class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ["id", "description"]

class DishSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dish
        fields = '__all__'