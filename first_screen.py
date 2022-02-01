from kivy.app import App
from kivy.lang import Builder
from kivy.uix.gridlayout import GridLayout
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.screenmanager import Screen

Builder.load_file('first_screen.kv')


class FirstScreen(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.name = "first_screen"

    def pass_screen(self):
        # Computing is confidential
        pass


class GridLayoutMassVolume(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class CoupleAddDelete(RelativeLayout):
    def __init__(self, **kw):
        super().__init__(**kw)

    def add(self):
        app = App.get_running_app()
        data = app.variables
        var = data | {'text': str(data.get('machine')) + " - " + str(data.get('materiau_piece')) + " - " + str(
            data.get('materiau_support'))}

        app.screen_manager.get_screen('first_screen').ids.recycle_couple.data.append(var)
        print(app.screen_manager.get_screen('first_screen').ids.recycle_couple.data)

    def supp(self):
        app = App.get_running_app()
        print(app.screen_manager.get_screen('first_screen').ids.recycle_couple.data)

        if app.index is not None:
            app.screen_manager.get_screen('first_screen').ids.recycle_couple.data.pop(app.index)
