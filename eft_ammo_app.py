import pandas as pd
import matplotlib.pyplot as plt
import pymongo
import seaborn as sb
import numpy as np
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget
from kivy.lang import Builder

pd.set_option('display.max_columns', None)
ammo_df = pd.read_csv("ammo.csv")

#all unique ammo sizes
size_df = ammo_df["Size"].unique()

#filtering by size
ammo_df[ammo_df["Size"] == "12 Gauge Shot"]

########################## KIVY GUI #################################

class MyGrid(Widget):
    pass

class MyApp(App):
    def build(self):
        return MyGrid()

if __name__ == '__main__':
    MyApp().run()