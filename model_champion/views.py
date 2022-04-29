import json
import os
from django.http import JsonResponse
from django.shortcuts import render

from league.settings import BASE_DIR
from model_champion.tools.initial_setting import putChampions

# Create your views here.

def set_champion(request) :
    putChampions()
    return JsonResponse({}, json_dumps_params={'ensure_ascii':False})