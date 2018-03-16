from django.http import HttpResponse
from .models import RacingFactory

def index(request):
    
    racingWebsite = RacingFactory.getRacingWebsiteScraper("https://www.racingpost.com")
    
    allTodaysRaces = racingWebsite.getTodaysRaces()
    
    for eachRace in allTodaysRaces:
        
        allHorses = racingWebsite.getAllHorsesInARace(eachRace)
        
        for eachHorse in allHorses:
            racingWebsite.getHorseStatistics(eachHorse)

    return HttpResponse("ok")