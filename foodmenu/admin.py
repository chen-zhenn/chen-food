from django.contrib import admin
from foodmenu.models import Category, Culinary, Ingredient, Dish
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name", "deleted"]
    list_display_links = ["name"]

admin.site.register(Category, CategoryAdmin)

class CulinaryAdmin(admin.ModelAdmin):
    list_display = ["name", "deleted"]
    list_display_links = ["name"]

admin.site.register(Culinary, CulinaryAdmin)

class IngredientAdmin(admin.ModelAdmin):
    list_display = ["description", "deleted"]
    list_display_links = ["description", "deleted"]

admin.site.register(Ingredient, IngredientAdmin)

class DishAdmin(admin.ModelAdmin):
    list_display = ["name", "image", "description", "price", "category", "culinary", "ingredient", "deleted"]
    list_display_links = ["name", "image", "description", "price", "category", "culinary", "ingredient"]
    
admin.site.register(Dish, DishAdmin)
