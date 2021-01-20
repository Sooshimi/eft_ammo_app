import pandas as pd
import time
from bs4 import BeautifulSoup as soup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

pd.set_option('display.max_columns', None)

try:
    ammo_df = pd.read_csv("ammo.csv")
except:
    print("'ammo.csv' not in this python file's directory")

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
driver = webdriver.Chrome(PATH, options=options) #starts webdriver
driver.get("https://tarkov-market.com/tag/ammo") #opens url

# Get current scroll height
last_height = driver.execute_script("return document.body.scrollHeight")

while True:
    # Script to scroll down to bottom of page
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Wait to load page
    time.sleep(0.5)

    # gets new scroll height and compare with last scroll height
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
    price = handle(item.find("span", {"class": "price-main"}))
    temp[name] = price
    ammo_list.update(temp)

for key, value in ammo_list.items():
    print(key)

#replace all ammo_list dict keys with ref numbers (refer to ammo.csv)
ammo_list[1] = ammo_list.pop('12/70 5.25mm Buckshot')
ammo_list[2] = ammo_list.pop('12/70 8.5 mm "Magnum" Buckshot')
ammo_list[3] = ammo_list.pop('12x70 6.5 mm "Express" Buckshot')
ammo_list[4] = ammo_list.pop('12x70 7mm Buckshot')
ammo_list[5] = ammo_list.pop('12/70 Flechette')
ammo_list[6] = ammo_list.pop('9x19 mm RIP')
ammo_list[7] = ammo_list.pop('12/70 HP Slug "SuperFormance"')
ammo_list[8] = ammo_list.pop('12/70 Grizzly 40 Slug')
ammo_list[9] = ammo_list.pop('12/70 HP Slug Copper Sabot Premier')
ammo_list[10] = ammo_list.pop('12x70 Led slug')
ammo_list[11] = ammo_list.pop('12/70 Dual Sabot Slug')
ammo_list[12] = ammo_list.pop('12/70 "Poleva-3" Slug')
ammo_list[13] = ammo_list.pop('12/70 FTX Custom LIte Slug')
ammo_list[14] = ammo_list.pop('12/70 Dual Sabot Slug')
ammo_list[15] = ammo_list.pop('12x70 shell with .50 BMG bullet')
ammo_list[16] = ammo_list.pop('12/70 AP-20 Slug')
ammo_list[17] = ammo_list.pop('20/70 5.6mm Buckshot')
ammo_list[18] = ammo_list.pop('20/70 6.2mm Buckshot')
ammo_list[19] = ammo_list.pop('20x70 7.5mm Buckshot')
ammo_list[20] = ammo_list.pop('20/70 7.3mm Buckshot')
ammo_list[21] = ammo_list.pop('20/70 Devastator Slug')
ammo_list[22] = ammo_list.pop('20/70 Slug "Poleva-3"')
ammo_list[23] = ammo_list.pop('20/70 Star Slug')
ammo_list[24] = ammo_list.pop('12/70 "Poleva-6u" Slug')
ammo_list[25] = ammo_list.pop('23x75mm "Star"')
ammo_list[26] = ammo_list.pop('23x75mm Shrapnel-25')
ammo_list[27] = ammo_list.pop('23x75mm Shrapnel 10')
ammo_list[28] = ammo_list.pop('23x75mm "Barricade"')
ammo_list[29] = ammo_list.pop('9x18 mm PM SP8 gzh')
ammo_list[30] = ammo_list.pop('9x18 mm PM SP7 gzh')
ammo_list[31] = ammo_list.pop('9x18 mm PM PSV')
ammo_list[32] = ammo_list.pop('9x18 mm PM 9 P gzh')
ammo_list[33] = ammo_list.pop('9x19 mm PSO gzh')
ammo_list[34] = ammo_list.pop('9x18 mm PM PS gs PPO')
ammo_list[35] = ammo_list.pop('9x18 mm PM PRS gs')
ammo_list[36] = ammo_list.pop('9x18 mm PM PPe gzh')
ammo_list[37] = ammo_list.pop('9x18 mm PM PPT gzh')
ammo_list[38] = ammo_list.pop('9x18 mm PM Pst gzh')
ammo_list[39] = ammo_list.pop('9x18mm PM RG028 gzh')
ammo_list[40] = ammo_list.pop('9x18 mm PM 9 BZT gzh')
ammo_list[41] = ammo_list.pop('9x18 mm PM PMM')

ammo_list[44] = ammo_list.pop('7.62x25mm TT LRN')
ammo_list[51] = ammo_list.pop('9x19 mm QuakeMaker')
ammo_list[52] = ammo_list.pop('9x19 mm PSO gzh')
ammo_list[59] = ammo_list.pop('.45 ACP Hydra-Shok')
ammo_list[60] = ammo_list.pop('.45 ACP Lasermatch FMJ')
ammo_list[61] = ammo_list.pop('.45 ACP FMJ')
ammo_list[65] = ammo_list.pop('9x21 mm SP10')
ammo_list[74] = ammo_list.pop('4.6x30mm Action SX')
ammo_list[75] = ammo_list.pop('4.6x30mm Subsonic SX')
ammo_list[102] = ammo_list.pop('5.56x45 mm 55 FMJ')
ammo_list[107] = ammo_list.pop('7.62x39 mm HP')
ammo_list[109] = ammo_list.pop('7.62x39 mm T45M')
ammo_list[133] = ammo_list.pop('.338 Lapua Magnum AP')

#add dict values (prices) to new df column 'Price', on key values
ammo_df["Price"] = ammo_df["Ref"].apply(lambda x: ammo_list.get(x))