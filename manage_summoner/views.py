from django.http import JsonResponse
from django.shortcuts import render
from secret import LEAUGE_OF_LEGEND_API_KEY as key
import requests

def enquiry(request) :
    return render(request, 'enquiry.html', {})

def summoner_name(request) :
    summoner = request.GET['q']
    riot_status_url = "https://kr.api.riotgames.com/lol/summoner/v4/summoners/by-name/" + summoner
    response = requests.get(riot_status_url, headers={"X-Riot-Token": key}) 
    summonerDict = response.json()

    riot_status_url = "https://kr.api.riotgames.com/lol/champion-mastery/v4/champion-masteries/by-summoner/" + summonerDict['id']
    response = requests.get(riot_status_url, headers={"X-Riot-Token": key}) 
    masteryList = response.json()
    return render(request, 'summoner_name.html', {"summoner" : summoner, "summonerDict" : summonerDict, "masteryList" : masteryList, "masteryLen" : len(masteryList)})

# Create your views here.
