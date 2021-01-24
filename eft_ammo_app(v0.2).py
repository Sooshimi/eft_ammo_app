import pandas as pd
import time
from bs4 import BeautifulSoup as soup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import tkinter as tk
from tkinter import ttk
from matplotlib import pyplot as plt

pd.set_option('display.max_columns', None)

try:
    ammo_df = pd.read_csv("ammo.csv")
except:
    print("'ammo.csv' not in this python file's directory")

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
    time.sleep(1)

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

#replace all ammo_list dict keys with ref numbers (refer to ammo.csv)
ammo_list[1] = ammo_list.pop('12/70 5.25mm Buckshot')
ammo_list[2] = ammo_list.pop('12/70 8.5 mm "Magnum" Buckshot')
ammo_list[3] = ammo_list.pop('12x70 6.5 mm "Express" Buckshot')
ammo_list[4] = ammo_list.pop('12x70 7mm Buckshot')
ammo_list[5] = ammo_list.pop('12/70 Flechette')
ammo_list[6] = ammo_list.pop('12x70 RIP')
ammo_list[7] = ammo_list.pop('12/70 HP Slug "SuperFormance"')
ammo_list[8] = ammo_list.pop('12/70 Grizzly 40 Slug')
ammo_list[9] = ammo_list.pop('12/70 HP Slug Copper Sabot Premier')
ammo_list[10] = ammo_list.pop('12x70 Led slug')
ammo_list[11] = ammo_list.pop('12/70 Dual Sabot Slug')
ammo_list[12] = ammo_list.pop('12/70 "Poleva-3" Slug')
ammo_list[13] = ammo_list.pop('12/70 FTX Custom LIte Slug')
ammo_list[14] = ammo_list.pop('12/70 "Poleva-6u" Slug')
ammo_list[15] = ammo_list.pop('12x70 shell with .50 BMG bullet')
ammo_list[16] = ammo_list.pop('12/70 AP-20 Slug')

ammo_list[17] = ammo_list.pop('20/70 5.6mm Buckshot')
ammo_list[18] = ammo_list.pop('20/70 6.2mm Buckshot')
ammo_list[19] = ammo_list.pop('20x70 7.5mm Buckshot')
ammo_list[20] = ammo_list.pop('20/70 7.3mm Buckshot')
ammo_list[21] = ammo_list.pop('20/70 Devastator Slug')
ammo_list[22] = ammo_list.pop('20/70 Slug "Poleva-3"')
ammo_list[23] = ammo_list.pop('20/70 Star Slug')
ammo_list[24] = ammo_list.pop('20/70 Slug Poleva-6u')

ammo_list[25] = ammo_list.pop('23x75mm "Star"')
ammo_list[26] = ammo_list.pop('23x75mm Shrapnel-25')
ammo_list[27] = ammo_list.pop('23x75mm Shrapnel 10')
ammo_list[28] = ammo_list.pop('23x75mm "Barricade"')

ammo_list[29] = ammo_list.pop('9x18 mm PM SP8 gzh')
ammo_list[30] = ammo_list.pop('9x18 mm PM SP7 gzh')
ammo_list[31] = ammo_list.pop('9x18 mm PM PSV')
ammo_list[32] = ammo_list.pop('9x18 mm PM 9 P gzh')
ammo_list[33] = ammo_list.pop('9x18 mm PM PSO gzh')
ammo_list[34] = ammo_list.pop('9x18 mm PM PS gs PPO')
ammo_list[35] = ammo_list.pop('9x18 mm PM PRS gs')
ammo_list[36] = ammo_list.pop('9x18 mm PM PPe gzh')
ammo_list[37] = ammo_list.pop('9x18 mm PM PPT gzh')
ammo_list[38] = ammo_list.pop('9x18 mm PM Pst gzh')
ammo_list[39] = ammo_list.pop('9x18mm PM RG028 gzh')
ammo_list[40] = ammo_list.pop('9x18 mm PM 9 BZT gzh')
ammo_list[41] = ammo_list.pop('9x18 mm PM PMM')
ammo_list[42] = ammo_list.pop('9x18 mm PM PBM')

ammo_list[43] = ammo_list.pop('7.62x25mm TT LRNPC')
ammo_list[44] = ammo_list.pop('7.62x25mm TT LRN')
ammo_list[45] = ammo_list.pop('7.62x25mm TT FMJ43')
ammo_list[46] = ammo_list.pop('7.62x25mm TT AKBS')
ammo_list[47] = ammo_list.pop('7.62x25mm TT P gl')
ammo_list[48] = ammo_list.pop('7.62x25mm TT PT gzh')
ammo_list[49] = ammo_list.pop('7.62x25mm TT Pst gzh')

ammo_list[50] = ammo_list.pop('9x19 mm RIP')
ammo_list[51] = ammo_list.pop('9x19 mm QuakeMaker')
ammo_list[52] = ammo_list.pop('9x19 mm PSO gzh')
ammo_list[53] = ammo_list.pop('9x19 mm Luger CCI')
ammo_list[54] = ammo_list.pop('9x19 mm Green Tracer')
ammo_list[55] = ammo_list.pop('9x19 mm Pst gzh')
ammo_list[56] = ammo_list.pop('9x19 mm AP 6.3')
ammo_list[57] = ammo_list.pop('9x19 mm 7N31')

ammo_list[58] = ammo_list.pop('.45 RIP')
ammo_list[59] = ammo_list.pop('.45 ACP Hydra-Shok')
ammo_list[60] = ammo_list.pop('.45 ACP Lasermatch FMJ')
ammo_list[61] = ammo_list.pop('.45 ACP FMJ')
ammo_list[62] = ammo_list.pop('.45 ACP AP')

ammo_list[63] = ammo_list.pop('9x21 mm SP12')
ammo_list[64] = ammo_list.pop('9x21 mm SP11')
ammo_list[65] = ammo_list.pop('9x21 mm SP10')
ammo_list[66] = ammo_list.pop('9x21 mm SP13')

ammo_list[67] = ammo_list.pop('5.7x28 mm R37.F')
ammo_list[68] = ammo_list.pop('5.7x28 mm SS198LF')
ammo_list[69] = ammo_list.pop('5.7x28 mm R37.X')
ammo_list[70] = ammo_list.pop('5.7x28 mm SS197SR')
ammo_list[71] = ammo_list.pop('5.7x28 mm L191')
ammo_list[72] = ammo_list.pop('5.7x28 mm SB193')
ammo_list[73] = ammo_list.pop('5.7x28 mm SS190')

ammo_list[74] = ammo_list.pop('4.6x30mm Action SX')
ammo_list[75] = ammo_list.pop('4.6x30mm Subsonic SX')
ammo_list[76] = ammo_list.pop('4.6x30mm FMJ SX')
ammo_list[77] = ammo_list.pop('4.6x30mm AP SX')

ammo_list[78] = ammo_list.pop('9x39 mm SP-5')
ammo_list[79] = ammo_list.pop('9x39 mm SP-6')
ammo_list[80] = ammo_list.pop('9x39 mm 7N9 SPP')
ammo_list[81] = ammo_list.pop('9x39 mm 7N12 BP')

ammo_list[82] = ammo_list.pop('.366 TKM Geksa')
ammo_list[83] = ammo_list.pop('.366 TKM FMJ')
ammo_list[84] = ammo_list.pop('.366 TKM EKO')
ammo_list[85] = ammo_list.pop('.366 AP')

ammo_list[86] = ammo_list.pop('5.45x39 mm SP')
ammo_list[87] = ammo_list.pop('5.45x39 mm HP')
ammo_list[88] = ammo_list.pop('5.45x39 mm PRS')
ammo_list[89] = ammo_list.pop('5.45x39 mm US')
ammo_list[90] = ammo_list.pop('5.45x39 mm FMJ')
ammo_list[91] = ammo_list.pop('5.45x39 mm T')
ammo_list[92] = ammo_list.pop('5.45x39 mm PS')
ammo_list[93] = ammo_list.pop('5.45x39 mm PP')
ammo_list[94] = ammo_list.pop('5.45x39 mm BP')
ammo_list[95] = ammo_list.pop('5.45x39 mm BT')
ammo_list[96] = ammo_list.pop('5.45x39 mm BS')
ammo_list[97] = ammo_list.pop('5.45x39 mm 7N39 "Igolnik"')

ammo_list[98] = ammo_list.pop('5.56x45mm Warmage')
ammo_list[99] = ammo_list.pop('5.56x45 mm 55 HP')
ammo_list[100] = ammo_list.pop('5.56x45 mm Mk 255 Mod 0')
ammo_list[101] = ammo_list.pop('5.56x45 mm M856')
ammo_list[102] = ammo_list.pop('5.56x45 mm 55 FMJ')
ammo_list[103] = ammo_list.pop('5.56x45 mm M855')
ammo_list[104] = ammo_list.pop('5.56x45 mm M856A1')
ammo_list[105] = ammo_list.pop('5.56x45 mm M855A1')
ammo_list[106] = ammo_list.pop('5.56x45 mm M995')

ammo_list[107] = ammo_list.pop('7.62x39 mm HP')
ammo_list[108] = ammo_list.pop('7.62x39 mm US')
ammo_list[109] = ammo_list.pop('7.62x39 mm T45M')
ammo_list[110] = ammo_list.pop('7.62x39 mm PS')
ammo_list[111] = ammo_list.pop('7.62x39 mm BP')

ammo_list[112] = ammo_list.pop('.300 BPZ AAC Blackout')
ammo_list[113] = ammo_list.pop('.300 AAC Blackout AP')

ammo_list[114] = ammo_list.pop('7.62x51 mm Ultra Nosler')
ammo_list[115] = ammo_list.pop('7.62x51 mm BPZ FMJ')
ammo_list[116] = ammo_list.pop('7.62x51 mm TPZ SP')
ammo_list[117] = ammo_list.pop('7.62x51 mm M80')
ammo_list[118] = ammo_list.pop('7.62x51 mm M62')
ammo_list[119] = ammo_list.pop('7.62x51 mm M61')
ammo_list[120] = ammo_list.pop('7.62x51 mm M993')

ammo_list[121] = ammo_list.pop('7.62x54R T-46M')
ammo_list[122] = ammo_list.pop('7.62x54R LPS Gzh')
ammo_list[123] = ammo_list.pop('7.62x54R 7N1 Sniper cartridge')
ammo_list[124] = ammo_list.pop('7.62x54R 7BT1')
ammo_list[125] = ammo_list.pop('7.62x54R SNB')
ammo_list[126] = ammo_list.pop('7.62x54R 7N37')

ammo_list[127] = ammo_list.pop('12.7x55 mm PS12A')
ammo_list[128] = ammo_list.pop('12.7x55 mm PS12')
ammo_list[129] = ammo_list.pop('12.7x55 mm PS12B')

ammo_list[130] = ammo_list.pop('.338 Lapua Magnum TAC-X')
ammo_list[131] = ammo_list.pop('.338 UPZ Lapua Magnum')
ammo_list[132] = ammo_list.pop('.338 Lapua Magnum FMJ')
ammo_list[133] = ammo_list.pop('.338 Lapua Magnum AP')

ammo_list[134] = ammo_list.pop('30x29 mm VOG-30')

ammo_list[137] = ammo_list.pop('40x46 mm M576(MP-APERS)')

#add dict values (prices) to new df column 'Price', on key values
ammo_df["Price"] = ammo_df["Ref"].apply(lambda x: ammo_list.get(x))

ammo_df = ammo_df.drop(columns=["Ref","Ref2"])

class MyApp(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        # self.s = ttk.Style()
        # self.s.theme_use('alt')

        self.f1 = ttk.Frame(master)
        self.f1.grid(row=0, column=1, sticky="nw", padx=5, pady=5, columnspan=2)
        self.create_button(self.f1, "All", 0, 0, "nw", 5, 5, width=16)

        self.f2 = ttk.Frame(master)
        self.f2.grid(row=1, column=0, sticky="nw", padx=5, pady=5, columnspan=2)
        self.create_button(self.f2, "12 Gauge Shot", 0, 0, "nw", 5, 0)
        self.create_button(self.f2, "12 Gauge Slugs", 1, 0, "nw", 5, 0)
        self.create_button(self.f2, "20 Gauge", 2, 0, "nw", 5, (0,10))
        self.create_button(self.f2, "9x18mm", 3, 0, "nw", 5, 0)
        self.create_button(self.f2, "9x19mm", 4, 0, "nw", 5, 0)
        self.create_button(self.f2, "9x21mm", 5, 0, "nw", 5, 0)
        self.create_button(self.f2, "9x39mm", 6, 0, "nw", 5, (0,10))
        self.create_button(self.f2, "0.366", 7, 0, "nw", 5, 0)
        self.create_button(self.f2, "0.388", 8, 0, "nw", 5, 0)
        self.create_button(self.f2, "0.45", 9, 0, "nw", 5, (0,10))
        self.create_button(self.f2, "Mounted Weapons", 10, 0, "nw", 5, 0)
        self.create_button(self.f2, "Other", 11, 0, "nw", 5, 0)

        self.f3 = ttk.Frame(master)
        self.f3.grid(row=1, column=2, sticky="nw", padx=5, pady=5, columnspan=2)
        self.create_button(self.f3, "4.6x30mm", 0, 0, "nw", 5, (0,11))
        self.create_button(self.f3, "5.45x39mm", 1, 0, "nw", 5, 0)
        self.create_button(self.f3, "5.56x45mm", 2, 0, "nw", 5, 0)
        self.create_button(self.f3, "5.7x28mm", 3, 0, "nw", 5, (0,11))
        self.create_button(self.f3, "7.62x25mm", 4, 0, "nw", 5, 0)
        self.create_button(self.f3, "7.62x39mm", 5, 0, "nw", 5, 0)
        self.create_button(self.f3, "7.62x51mm", 6, 0, "nw", 5, 0)
        self.create_button(self.f3, "7.62x54R", 7, 0, "nw", 5, (0,11))
        self.create_button(self.f3, "23x75mm", 8, 0, "nw", 5, (0, 11))
        self.create_button(self.f3, "12.7x55mm", 9, 0, "nw", 5, (0, 11))
        self.create_button(self.f3, "300 BLK", 10, 0, "nw", 5, 0)

        self.f4 = ttk.Frame(master)
        self.f4.grid(row=0, column=1, sticky="nw", padx=5, pady=5, columnspan=1)

    def create_button(self, master, text="", row=0, col=0, sticky="nw", padx=0, pady=0, colspan=1, width=16):
        self.master = master
        self.button = ttk.Button(master, text=text, width=width)
        self.button.grid(row=row, column=col, sticky=sticky, padx=padx, pady=pady, columnspan=colspan)


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Snackbox")
    root.geometry("1200x400")
    app = MyApp(master=root)
    app.mainloop()