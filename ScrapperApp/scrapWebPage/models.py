from django.db import models

from abc import ABC, abstractmethod
from bs4 import BeautifulSoup
from .scrapperUtils import getHTMLPageUsingSelenium, getHTMLPage
import re
import json, requests

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
    
    def getHorseStatistics(self,horse):
        indexTabInsert = horse.find('/horse/')
        horseJsonFormUrl = horse[:indexTabInsert] + '/tab' + horse[indexTabInsert:horse.rfind('#')] + '/form'
        resp = requests.get(url=horseJsonFormUrl)
        data = json.loads(resp.text)
        
        for key, val in data['form'].items():
            course_id = key
            course_name = val['courseName']
            classType = val['raceClass']
            euroPrize = val['prizeEuro']
            sterlingPrize = val['prizeSterling']
            distanceYard = val['distanceYard']
            distanceFurlong = val['distanceFurlong']
            distanceToWinnerLengths = val['distanceToWinner']
    
    def getBaseURL(self):
        return self.baseURL