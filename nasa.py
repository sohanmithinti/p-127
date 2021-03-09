from selenium import webdriver
from bs4 import BeautifulSoup
import time
import csv

start_url = "https://exoplanets.nasa.gov/discovery/exoplanet-catalog/"
browser = webdriver.Chrome("/sohan_whjr/nasa/chromedriver")
browser.get(start_url)
time.sleep(10)

def scrap():
    header = ["name", "light_years", "planet_mass", "stellar_magnitude", "discovery_date"]
    soup = BeautifulSoup(browser.page_source, "html.parser")
    for ultag in soup.find_all("ul", attrs = {"class", "exoplanet"}): 
        li_tags = ultag.find_all("li")
        list1 = []
        planet_data = []
        for index, litag in enumerate(li_tags):
            if(index == 0):
                list1.append(litag.find_all("a")[0].contents[0])
            else:
                try:
                    list1.append(litag.contents[0])
                except:
                    list1.append("")
      
        planet_data.append(list1)
        print(planet_data)

scrap()    