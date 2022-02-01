from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
import csv

from kivy.uix.textinput import TextInput

from first_screen import FirstScreen
from machines import Machine
from predixio_widgets.recyclerview import RecycleMachines
from predixio_widgets.recyclerview import RecycleMaterial
from predixio_widgets.recyclerview import RecycleCouple

variables = dict({
    'machine': None,
    'materiau_piece': None,
    'materiau_support': None,
    'temps': None,
    'hauteur_de_couche': None,
    'angle': None,
    'mv_piece': "masse",
    'mv_piece_value': None,
    'mv_support': "masse",
    'mv_support_value': None

})



class PredixioScreenManager(ScreenManager):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.add_widget(FirstScreen())


class PredixioApp(App):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.screen_manager = PredixioScreenManager()
        self.couple = []
        self.machine = ""
        self.material_piece = ""
        self.material_support = ""
        self.index = None
        self.variables = variables

    def build(self):
        return self.screen_manager


if __name__ == "__main__":
    PredixioApp().run()
