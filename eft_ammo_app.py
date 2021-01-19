import pandas as pd
import matplotlib.pyplot as plt
import pymongo
import seaborn as sb
import numpy as np
import time
import re
from bs4 import BeautifulSoup as soup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

pd.set_option('display.max_columns', None)
ammo_df = pd.read_csv("ammo.csv")

#all unique ammo sizes
size_df = ammo_df["Size"].unique()

#all unique ammo types
type_df = ammo_df["Ammo Type"].unique()

#filtering by size
ammo_df[ammo_df["Size"] == "12 Gauge Shot"]

# function to handle below AttributeError, and gets text and strips extra spaces
# AttributeError: 'NoneType' object has no attribute 'html'
def handle(find):
    if find is not None: # checks if container is a NoneType
        info = find.text.strip() # gets text and strips extra spaces
    else:
        info = "" # if NoneType, replace with empty string
    return info

PATH = "C:\Program Files (x86)\chromedriver.exe" #path of local chromedrive
options = Options()
options.headless = True #headless chromedriver
driver = webdriver.Chrome(PATH, options=options)
driver.get("https://tarkov-market.com/tag/ammo")

# Get current scroll height
last_height = driver.execute_script("return document.body.scrollHeight")

scroll_pause_time = 0.5
while True:
    # Script to scroll down to bottom of page
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Wait to load page
    time.sleep(scroll_pause_time)

    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height

html = driver.page_source #get page source
driver.quit() #quit selenium driver

page_soup = soup(html, "html.parser") # beautifulsoup html parser

#grabs each item (ammo)
items = page_soup.findAll({"tr":"data-v-5b3a2888"}, {"class":"item"})

ammo_list = {} # {name:price}

#look through all items and append the ammo name and price to a dictionary
for item in items:
    temp = {}
    name = handle(item.find("span", {"class": "name"}))
    price = handle(item.find("span",{"class": "price-main"}))
    temp[name] = price
    ammo_list.update(temp)

for key, value in ammo_list.items():
    print(key)

#replace all ammo_list dict keys with refs (refer to csv)
ammo_list["12x70 shell with .50 BMG bullet"] = 15
ammo_list["9x19 mm PSO gzh"] = 52
ammo_list["12/70 Dual Sabot Slug"] = 14