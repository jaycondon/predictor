from abc import ABC, abstractmethod
from bs4 import BeautifulSoup
from .scrapperUtils import getHTMLPageUsingSelenium, getHTMLPage
import re
import json, requests
from django.db import models
# import the logging library
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)

class RacingFactory(object):
    @staticmethod
    def getRacingWebsiteScraper(baseURL):
        if baseURL == "https://www.racingpost.com":
            return RacingPost(baseURL)

class HorseRacingWebsite(ABC):
    
    def __init__(self,baseURL):
        pass
    
    @abstractmethod
    def getTodaysRaces(self):
        pass
    
    @abstractmethod
    def getAllHorsesInARace(self,race):
        pass
    
    @abstractmethod
    def getHorseStatistics(self,horse):
        pass
    
    @abstractmethod
    def getBaseURL(self):
        return self.baseURL
    
    def convertSterling(self,sterling_value):
        return sterling_value * 1.13
    
    def convertFurlongToMeters(self,furlongs):
        return furlongs * 201.168
    
    def convertYardsToMeters(self,yards):
        return yards * 0.9144
    

class RacingPost(HorseRacingWebsite):
    
    
    
    def __init__(self,baseURL):
        self.baseURL = baseURL
    
    def getTodaysRaces(self):
        htmlpage = getHTMLPageUsingSelenium(self.getBaseURL())
        parsedHTML = BeautifulSoup(htmlpage, "lxml")
        
        raceLinksRegEx = re.compile("rh-cardsMatrix__time ui-link rh-cardsMatrix__time_race js-navigate-url rh-cardsMatrix_color[0-9]*")
        allTodaysRacesLinks = parsedHTML.findAll("a",class_=raceLinksRegEx)

        listOfLinks = []
        for eachRaceLink in allTodaysRacesLinks:
            link = self.baseURL + eachRaceLink["href"]
            listOfLinks.append(link)
        
        return listOfLinks
    
    def getAllHorsesInARace(self, race):
        htmlpage = getHTMLPage(race)
        parsedHTML = BeautifulSoup(htmlpage, "lxml")
        allHorsesTagsInRace = parsedHTML.findAll("a",class_="RC-runnerName ui-link js-popupLink js-bestOddsRunnerHorseName")
        
        listOfHorses = []
        for eachHorse in allHorsesTagsInRace:
            link = self.baseURL + eachHorse["href"]
            listOfHorses.append(link)
        
        return listOfHorses
    
    def saveHorse(self,horse_url):
        javascriptPage = getHTMLPageUsingSelenium(horse_url)
        if javascriptPage is None:
            return 
        parsedHTML = BeautifulSoup(javascriptPage, "lxml")
        horseNameTag = parsedHTML.find("h1",class_="hp-nameRow__name")
        horse_name = re.sub("[^a-zA-Z ]",'', horseNameTag.text)
        horse_name = horse_name.strip()
        
        horse = None
        try:
            horse = Horse.objects.get(name=horse_name)
        except:
            logger.debug("There is no horse by the name: " + horse_name)
        
        if horse is None: 
            horse_age = parsedHTML.find("dt",class_="pp-definition__term")
            ageText = re.sub('[^0-9]*','', horse_age.text)
            horse = Horse(name = horse_name, age = int(ageText))
            horse.save()
        
        return horse
    
    def saveRace(self,race_json):
        race_name = race_json['courseName']
        race_date = race_json['raceDatetime']
        
        race = None
        try:
            race = Horse.objects.get(name=race_name, date = race_date)
        except:
            logger.debug("There is no race in: " + race_name + " at " + race_date)
        if race is None:
            if race_json['prizeEuro'] != 0:
                    race_prize = race_json['prizeEuro']
            else:
                race_prize = self.convertSterling(race_json['prizeSterling'])
            distance_meters = int(self.convertFurlongToMeters(race_json['distanceFurlong']))
            race_going = race_json['goingTypeCode']
            race_group = race_json['raceGroupDesc']
            r_class = race_json['raceClass']
            total_runners = race_json['noOfRunners']
            race = Race(name = race_name,prize = race_prize, date = race_date, going = race_going, group = race_group, race_class = r_class, no_runners = total_runners, distance = distance_meters)
            race.save()
        return race
    
    def linkRaceAndHorse(self,horse_obj,race_obj,json):
        
        link_horse_and_race = None
        try:
            link_horse_and_race = Horse.objects.get(horse=horse_obj, race = race_obj)
        except:
            logger.debug("There is no link for: " + horse_obj.name + " and " + race_obj.name)
        
        
        if link_horse_and_race is None:
            link_comment = json['rpCloseUpComment']
            link_distance = self.convertYardsToMeters(json['distanceYard'])
            link_draw = json['draw']
            link_position = json['raceOutcomeCode']
            link_weight_carried = json['weightCarriedLbs']
            horseRaceLink = HorseRaceLink(horse=horse_obj,race=race_obj,comment=link_comment,distance=link_distance,draw=link_draw,position=link_position,weight_carried=link_weight_carried)
            horseRaceLink.save()
        
    def getHorseStatistics(self,horse_url):
        horse = None
        try:
            horse = self.saveHorse(horse_url)
        except Exception as e:
            logger.error("Error while trying to save horse at this url: " + horse_url)
            logger.error(e)
        
        if horse is None:
            return
        indexTabInsert = horse_url.find('/horse/')
        horseJsonFormUrl = horse_url[:indexTabInsert] + '/tab' + horse_url[indexTabInsert:horse_url.rfind('#')] + '/form'
        resp = requests.get(url=horseJsonFormUrl)
        data = json.loads(resp.text)
        
        for key, val in data['form'].items():
            race = None
            try:
                race = self.saveRace(val)
            except Exception as e:
                logger.error("Error while trying to save race " + key + " for url " + horseJsonFormUrl)
                logger.error(e)
            
            if race is None:
                continue
            
            try:
                self.linkRaceAndHorse(horse,race,val)
            except Exception as e:
                logger.error("Error while trying to link horse " + horse.name + " to race " + race.name)
                logger.error(e)
    
    def getBaseURL(self):
        return self.baseURL
    
class Race(models.Model):
    name = models.CharField(max_length=70)
    prize = models.DecimalField(max_digits=10, decimal_places=2)
    going = models.CharField(max_length=30)
    date = models.DateTimeField()
    group = models.CharField(max_length=10, default='~UNKNOWN',null=True)
    race_class = models.CharField(max_length=10, default='~UNKNOWN',null=True)
    no_runners = models.IntegerField()
    distance = models.CharField(max_length=15)
    
    def __str__(self):
        return self.name
    
class Horse(models.Model):
    name = models.CharField(unique=True,max_length=30)
    age = models.IntegerField()
    total_prize = models.DecimalField(max_digits=10, decimal_places=2,default=0)
    total_wins = models.IntegerField(default=0)
    total_placed = models.IntegerField(default=0)
    
    def __str__(self):
        return self.name
    
class HorseRaceLink(models.Model):
    horse = models.ForeignKey(Horse, on_delete=models.CASCADE)
    race = models.ForeignKey(Race, on_delete=models.CASCADE)
    comment = models.CharField(max_length=255,default='~UNKNOWN',null=True)
    distance = models.IntegerField()
    draw = models.IntegerField(null=True)
    position = models.CharField(max_length=10,default='~UNKNOWN')
    weight_carried = models.IntegerField()