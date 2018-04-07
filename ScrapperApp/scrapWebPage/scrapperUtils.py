'''
Created on Mar 3, 2018

@author: johnny
'''
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import requests
import logging


logger = logging.getLogger(__name__)

def getHTMLPage(pageLink):
    page = requests.get(pageLink)
    return page.content

def getHTMLPageUsingSelenium(pageLink):
    options = Options()
    options.binary = "/usr/bin/firefox"
    options.set_headless()
    options.add_argument("-purgecaches")
    driver = None
    pageSource = None
    try:
        driver = webdriver.Firefox(executable_path='/home/johnny/Desktop/geckodriver', firefox_binary='/usr/bin/firefox',options=options)
        driver.get(pageLink)
        pageSource = driver.page_source
    except Exception:
        logger.error("Error while trying to get page " + pageLink + " using Selenium in scrapperUtils.getHTMLPageUsingSelenium(pageLink)")
    finally:
        if driver is not None:
            driver.quit()
    return pageSource
    