from django.urls import path
from test_lol_api import views
urlpatterns = [
    path('api', views.test_api)
]