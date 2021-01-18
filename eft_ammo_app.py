import pandas as pd
import matplotlib.pyplot as plt
import pymongo
import seaborn as sb
import numpy as np
# from kivy.app import App
# from kivy.uix.button import Button

pd.set_option('display.max_columns', None)
ammo_df = pd.read_csv("ammo.csv")

#all unique ammo sizes
size_df = ammo_df["Size"].unique()

g_shot_12 = ammo_df[ammo_df["Size"] == "12 Gauge Shot"]

########################## KIVY GUI #################################

# class TestApp(App):
#     def build(self):
#         return Button(text='Hello World')
#
# TestApp().run()