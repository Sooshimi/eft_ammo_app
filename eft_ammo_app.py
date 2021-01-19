import pandas as pd
import matplotlib.pyplot as plt
import pymongo
import seaborn as sb
import numpy as np

pd.set_option('display.max_columns', None)
ammo_df = pd.read_csv("ammo.csv")

#all unique ammo sizes
size_df = ammo_df["Size"].unique()

#filtering by size
ammo_df[ammo_df["Size"] == "12 Gauge Shot"]

print(ammo_df.head())