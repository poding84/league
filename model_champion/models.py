from django.db import models


class Champion(models.Model):
    key = models.IntegerField(primary_key=True)
    id = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    lore = models.TextField()
    blurb = models.TextField()
    allytips = models.TextField()
    enemytips = models.TextField()
    tags = models.CharField(max_length=100)
    partype = models.CharField(max_length=100)

class ChampionInfo(models.Model) :
    champion = models.ForeignKey(Champion, on_delete=models.CASCADE)
    attack = models.IntegerField()
    defense = models.IntegerField()
    magic = models.IntegerField()
    difficulty = models.IntegerField()

class ChampionStat(models.Model):
    champion = models.ForeignKey(Champion, on_delete=models.CASCADE)
    hp = models.IntegerField()
    hpperlevel = models.IntegerField()
    mp = models.IntegerField()
    mpperlevel = models.IntegerField()
    movespeed = models.IntegerField()
    armor = models.IntegerField()
    armorperlevel = models.IntegerField()
    spellblock = models.IntegerField()
    spellblockperlevel = models.IntegerField()
    attackrange = models.IntegerField()
    hpregen = models.IntegerField()
    hpregenperlevel = models.IntegerField()
    mpregen = models.IntegerField()
    mpregenperlevel = models.IntegerField()
    crit = models.IntegerField()
    critperlevel = models.IntegerField()
    attackdamage = models.IntegerField()
    attackdamageperlevel = models.IntegerField()
    attackspeedperlevel = models.IntegerField()
    attackspeed = models.IntegerField()

class ChampionSpell(models.Model):
    champion = models.ForeignKey(Champion, on_delete=models.CASCADE)
    id = models.CharField(max_length=100, primary_key=True)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    tooltip = models.TextField()
    maxrank = models.IntegerField()
    cooldown = models.CharField(max_length=100)
    cooldownBurn= models.CharField(max_length=100)
    cost = models.CharField(max_length=100)
    costBurn = models.CharField(max_length=100)
    costType = models.CharField(max_length=100)
    range = models.CharField(max_length=100)
    resource = models.CharField(max_length=100)

class SpellImage(models.Model):
    spell = models.ForeignKey(ChampionSpell, on_delete=models.CASCADE)
    full = models.CharField(max_length=100)
    sprite = models.CharField(max_length=100)
    group = models.CharField(max_length=100)
    x = models.IntegerField()
    y = models.IntegerField()
    W = models.IntegerField()
    h = models.IntegerField()

class ChampionPassive(models.Model) :
    champion = models.ForeignKey(Champion, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()

class PassiveImage(models.Model) :
    passive = models.ForeignKey(ChampionPassive, on_delete=models.CASCADE)
    full = models.CharField(max_length=100)
    sprite = models.CharField(max_length=100)
    group = models.CharField(max_length=100)
    x = models.IntegerField()
    y = models.IntegerField()
    W = models.IntegerField()
    h = models.IntegerField()

class ChampionImage(models.Model) :
    champion = models.ForeignKey(Champion, on_delete=models.CASCADE)
    full = models.CharField(max_length=100)
    sprite = models.CharField(max_length=100)
    group = models.CharField(max_length=100)
    x = models.IntegerField()
    y = models.IntegerField()
    W = models.IntegerField()
    h = models.IntegerField()

class ChampionSkin(models.Model) :
    champion = models.ForeignKey(Champion, on_delete=models.CASCADE)
    id = models.CharField(max_length=100, primary_key=True)
    num = models.IntegerField()
    name = models.CharField(max_length=100)
    chromas = models.BooleanField()

