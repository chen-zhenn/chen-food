from django.urls import path
from foodmenu.views import index

urlpatterns = [
    path('', index),
]