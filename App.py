from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
import requests
import json

Window.size = (350,500)

class Ui(ScreenManager):
    indexRed = (1,0,0,1)
    indexGreen = (0,1,0,1)
    indexBlue = (0,0,1,1)
    num = 14
    #mandar por firebase
    logic = [1,1,1,0,1,0,1,0,1,0,1,0,2,2]
    x=0
    mat = [0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    while x<=num-1:
        if logic[x] == 1:
            mat[x] = indexGreen
        elif logic[x] == 0:
            mat[x] = indexRed
        else:
            mat[x] = indexBlue
        x=x+1
    
    pass
class MainApp(MDApp):
    firebase_url = 'https://visioncv-5ba27-default-rtdb.firebaseio.com/.json'

    def build(self):
        self.theme_cls.theme_style = 'Light'
        self.theme_cls.primary_palette = 'Teal'
        Builder.load_file('mainapp.kv')
        return Ui()
    
    def change_style(self,checked,value):
        if value:
            self.theme_cls.theme_style = 'Dark'
        else:
            self.theme_cls.theme_style = 'Light' 
    
if __name__ == "__main__":
    MainApp().run()


