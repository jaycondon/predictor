'''
Created on Mar 3, 2018

@author: johnny
'''
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import requests

def getHTMLPage(pageLink):
    page = requests.get(pageLink)
    return page.content

def getHTMLPageUsingSelenium(pageLink):
    options = Options()
    options.binary = "/usr/bin/firefox"
    options.set_headless()
    options.add_argument("-purgecaches")
    
    driver = webdriver.Firefox(executable_path='/home/johnny/Desktop/geckodriver', firefox_binary='/usr/bin/firefox',options=options)
    driver.get(pageLink)
    return driver.page_source
    