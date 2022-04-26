from django.shortcuts import render
from django.http import JsonResponse

from secret import LEAUGE_OF_LEGEND_API_KEY as key
import requests

# Create your views here.

def test_api(request) :
    riot_status_url = "https://kr.api.riotgames.com/lol/status/v4/platform-data"
    response = requests.get(riot_status_url, headers={"X-Riot-Token": key}) 
    return render(request, 'status.html', {"statusDict" : response.json()})
    # return JsonResponse({"riot_server_status" : response.json()}, json_dumps_params={'ensure_ascii':False})