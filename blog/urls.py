from django.urls import path
from . import views  # Importuješ views z blog aplikace

urlpatterns = [
    path('', views.post_list, name='post_list'),  # Přiřazuješ URL k funkci post_list
]
