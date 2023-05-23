from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from foodmenu.serializers import CategorySerializer, CulinarySerializer, IngredientSerializer, DishSerializer
from foodmenu.models import Category, Culinary, Ingredient, Dish

# Create your views here.
def index(req):
    return render(req, 'index.html')

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CulinaryViewSet(viewsets.ModelViewSet):
    queryset = Culinary.objects.all()
    serializer_class = CulinarySerializer

class IngredientViewSet(viewsets.ModelViewSet):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer

class DishViewSet(viewsets.ModelViewSet):
    queryset = Dish.objects.all()
    serializer_class = DishSerializer
