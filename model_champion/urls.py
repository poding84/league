from django.urls import path
from model_champion import views

urlpatterns = [
    path('champion/set', views.set_champion),
]