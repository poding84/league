from django.urls import path
from manage_summoner import views
urlpatterns = [
    path('', views.enquiry),
    path('name', views.summoner_name),
]