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

# pd.set_option('display.max_columns', None)
# ammo_df = pd.read_csv("ammo.csv")
#
# #all unique ammo sizes
# size_df = ammo_df["Size"].unique()
#
# #filtering by size
# ammo_df[ammo_df["Size"] == "12 Gauge Shot"]
#
# print(size_df)

########################## KIVY GUI #################################

class MyGrid(GridLayout):
    def __init__(self, **kwargs): ## **kwargs = take unlimited amount of parameters
        super(MyGrid, self).__init__(**kwargs) #calls gridlayout constructor
        self.cols = 1  # set columns for the main grid

        self.inside = GridLayout() # second grid inside the main grid
        self.inside.cols = 2

        # Add widgets
        self.inside.add_widget(Label(text="First Name: "))
        self.fname = TextInput(multiline=False)
        self.inside.add_widget(self.fname)

        self.inside.add_widget(Label(text="Last Name: "))
        self.lname = TextInput(multiline=False)
        self.inside.add_widget(self.lname)

        self.inside.add_widget(Label(text="Email: "))
        self.email = TextInput(multiline=False)
        self.inside.add_widget(self.email)
        
        self.add_widget(self.inside)

        self.submit = Button(text="Submit", font_size=40)
        self.submit.bind(on_press=self.pressed)
        self.add_widget(self.submit)

    def pressed(self, instance):
        first = self.fname.text
        last = self.lname.text
        email = self.email.text

        print("Name: ", first, "\nLast Name: ", last, "\nEmail: ", email)
        self.fname.text = ""
        self.lname.text = ""
        self.email.text = ""

class MyApp(App):
    def build(self):
        return MyGrid()

if __name__ == '__main__':
    MyApp().run()