
import os
from django.http import JsonResponse
from django.shortcuts import render
from league.settings import BASE_DIR
import json
# Create your views here.

def champs(request) :
    with open(os.path.join(BASE_DIR, 'dragontail/12.8.1/data/ko_KR/champion.json'), encoding='UTF-8') as f:
        data = json.load(f)

    return render(request, 'champs.html', {"champs" : data['data']})
    #return JsonResponse({}, json_dumps_params={'ensure_ascii':False})

def championDetail(request, championName) :
    with open(os.path.join(BASE_DIR, 'dragontail/12.8.1/data/ko_KR/champion/' + championName + ".json"), encoding='UTF-8') as f:
        data = json.load(f)
    
    
    return render(request, 'details.html', {"championName" : championName, "detail" : data})