from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from foodmenu.views import CategoryViewSet, CulinaryViewSet, IngredientViewSet, DishViewSet

router = routers.DefaultRouter()
router.register("category", CategoryViewSet)
router.register("culinary", CulinaryViewSet)
router.register("ingredient", IngredientViewSet)
router.register("dish", DishViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
