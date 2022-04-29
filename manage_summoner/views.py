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
    masteryStat = [0 for i in range(8)]
    masteryAvg = [0 for i in range(8)]
    for mastery in masteryList :
        masteryStat[mastery['championLevel']] += 1
        masteryAvg[mastery['championLevel']] += mastery['championPoints']

    return render(request, 'summoner_name.html', 
        {"summoner" : summoner, 
        "summonerDict" : summonerDict, 
        "masteryList" : masteryList, 
        "masteryLen" : len(masteryList),
        "masteryStat" : masteryStat[1:],
        "masteryAvg" : masteryAvg[1:]
    }
    )

# Create your views here.
