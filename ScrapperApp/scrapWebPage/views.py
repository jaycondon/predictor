from django.http import HttpResponse
from .models import RacingFactory
from time import gmtime, strftime
import logging

logger = logging.getLogger(__name__)

def index(request):
    
    racingWebsite = RacingFactory.getRacingWebsiteScraper("https://www.racingpost.com")
    
#    allTodaysRaces = racingWebsite.getTodaysRaces()
    
    current_time = strftime("%d-%m-%Y %H:%M:%S", gmtime())
    logger.info("Starting to crawl " + racingWebsite.getBaseURL() + " at " + current_time)

#     for eachRace in allTodaysRaces:
#         
#         allHorses = racingWebsite.getAllHorsesInARace(eachRace)
#         for eachHorse in allHorses:
#             try:
#                 racingWebsite.getHorseStatistics(eachHorse)
#             except Exception as e:
#                 logger.error(e)
                
    logger.info("Finished crawling " + racingWebsite.getBaseURL() + " at " + current_time)

    return HttpResponse("ok")

def hello(request):
    return HttpResponse("hello")