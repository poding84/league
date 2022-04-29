from django.urls import path
from test_lol_api import views
urlpatterns = [
    path('api', views.test_api),
    path('summoner/<str:summonerName>', views.test_summoner_name),
]