from django.shortcuts import render
from django.http import Http404, HttpResponseNotFound, JsonResponse

from secret import LEAUGE_OF_LEGEND_API_KEY as key
import requests

# Create your views here.

def test_api(request) :
    riot_status_url = "https://kr.api.riotgames.com/lol/status/v4/platform-data"
    response = requests.get(riot_status_url, headers={"X-Riot-Token": key}) 
    statusDict = response.json()
    print(response.status_code)
    if str(response.status_code) != '200' :
        return HttpResponseNotFound('server error')
    maintenanceList = []
    for maintenances in statusDict['maintenances'] :
        maintenanceList.append(maintenances)
        for updates in maintenanceList[-1]['updates'] :
            for content in updates['translations']: 
                if content['locale'] == 'ko_KR' :
                    updateDict = {
                        'content' : content['content'],
                        'locale' : content['locale']
                    }
                    updateDict.update(updates)
                    updateDict.pop('translations')
                    break
        maintenanceList[-1]['updates'] = updateDict
    statusDict['maintenances'] = maintenanceList
                

    return render(request, 'status.html', {"statusDict" : statusDict})
    # return JsonResponse({"riot_server_status" : response.json()}, json_dumps_params={'ensure_ascii':False})

def test_summoner_name(request, summonerName) :
    riot_status_url = "https://kr.api.riotgames.com/lol/summoner/v4/summoners/by-name/" + summonerName
    response = requests.get(riot_status_url, headers={"X-Riot-Token": key}) 
    return JsonResponse({"riot_server_status" : response.json()}, json_dumps_params={'ensure_ascii':False})
