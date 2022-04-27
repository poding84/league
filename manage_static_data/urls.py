from django.urls import path
from manage_static_data import views
urlpatterns = [
    path('champs', views.champs)
]