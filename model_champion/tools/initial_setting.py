

import json
import os
from typing import Dict

from league.settings import BASE_DIR
from model_champion.models import Champion, ChampionImage, ChampionInfo, ChampionPassive, ChampionSkin, ChampionSpell, ChampionStat, PassiveImage, SpellImage

def intListToStr(arr) :
    string = ""
    for a in arr :
        string += str(a) + ","
    return string

def putChampions() :
    with open(os.path.join(BASE_DIR, 'dragontail/12.8.1/data/ko_KR/championFull.json'), encoding='UTF-8') as f:
        data: Dict = json.load(f)['data']
    
    '''
    id, name, title, image{}, skins[{}], lore, blurb, allytips[], enemytips[], tags[], partype, info{}, stat{}, 
    spells[{
        id, name, description, leveltip{}, maxrank, cooldown[], cooldownBurn, cost[], costBurn, datavalues, effect[]*, effectBurn[]*, vars[]*, costType, range[], rangeBurn, image{}, resource
    }]
    passive{

    }
    '''
    return
    Champion.objects.all().delete()

    for key, value in data.items() :
        allytips = ""
        enemytips = ""
        tags = ""
        for string in value['allytips'] :
            allytips += string + ","

        for string in value['enemytips'] :
            enemytips += string + ","

        for string in value['tags'] :
            tags += string + ","

        champion = Champion.objects.create(
            key = value['key'],
            id = value['id'],
            name = value['name'],
            title = value['title'],
            lore = value['lore'],
            blurb = value['blurb'],
            allytips = allytips,
            enemytips = enemytips,
            tags = tags,
            partype = value['partype']
        )

        championImage = ChampionImage.objects.create(
            champion = champion,
            full = value['image']['full'],
            sprite = value['image']['sprite'],
            group = value['image']['group'],
            x = value['image']['x'],
            y = value['image']['y'],
            W = value['image']['w'],
            h = value['image']['h'],
        )

        skinBulkList = []
        for skin in value['skins'] :
            skinBulkList.append(ChampionSkin(
                champion = champion,
                id = skin['id'],
                num = skin['num'],
                name = skin['name'],
                chromas = skin['chromas'],
            ))
        ChampionSkin.objects.bulk_create(skinBulkList)

        championInfo = ChampionInfo.objects.create(
            champion = champion,
            attack = value['info']['attack'],
            defense = value['info']['defense'],
            magic = value['info']['magic'],
            difficulty = value['info']['difficulty']
        )

        championStat = ChampionStat.objects.create(
            champion = champion,
            hp = value['stats']['hp'],
            hpperlevel = value['stats']['hpperlevel'],
            mp = value['stats']['mp'],
            mpperlevel = value['stats']['mpperlevel'],
            movespeed = value['stats']['movespeed'],
            armor = value['stats']['armor'],
            armorperlevel = value['stats']['armorperlevel'],
            spellblock = value['stats']['spellblock'],
            spellblockperlevel = value['stats']['spellblockperlevel'],
            attackrange = value['stats']['attackrange'],
            hpregen = value['stats']['hpregen'],
            hpregenperlevel = value['stats']['hpregenperlevel'],
            mpregen = value['stats']['mpregen'],
            mpregenperlevel = value['stats']['mpregenperlevel'],
            crit = value['stats']['crit'],
            critperlevel = value['stats']['critperlevel'],
            attackdamage = value['stats']['attackdamage'],
            attackdamageperlevel = value['stats']['attackdamageperlevel'],
            attackspeedperlevel = value['stats']['attackspeedperlevel'],
            attackspeed = value['stats']['attackspeed'],
        )

        for spell in value['spells'] :
            championSpell = ChampionSpell.objects.create(
                champion = champion,
                id = spell['id'],
                name = spell['name'],
                description = spell['description'],
                tooltip = spell['tooltip'],
                maxrank = spell['maxrank'],
                cooldown = intListToStr(spell['cooldown']),
                cooldownBurn= spell['cooldownBurn'],
                cost = intListToStr(spell['cost']),
                costBurn = spell['costBurn'],
                costType = spell['costType'],
                range = intListToStr(spell['range']),
                resource = (spell['resource'] if 'resource' in spell else ''),
            )

            spellImage = SpellImage.objects.create(
                spell = championSpell,
                full = spell['image']['full'],
                sprite = spell['image']['sprite'],
                group = spell['image']['group'],
                x = spell['image']['x'],
                y = spell['image']['y'],
                W = spell['image']['w'],
                h = spell['image']['h'],
            )

        championPassive = ChampionPassive.objects.create(
            champion = champion,
            name = value['passive']['name'],
            description = value['passive']['description']
        )

        passiveImage = PassiveImage.objects.create(
            passive = championPassive,
            full = value['passive']['image']['full'],
            sprite = value['passive']['image']['sprite'],
            group = value['passive']['image']['group'],
            x = value['passive']['image']['x'],
            y = value['passive']['image']['y'],
            W = value['passive']['image']['w'],
            h = value['passive']['image']['h'],
        )

    
    return