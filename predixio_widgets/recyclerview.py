from kivy import app
from kivy.app import App
from kivy.lang import Builder
from kivy.properties import BooleanProperty
from kivy.uix.behaviors import FocusBehavior
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.recycleboxlayout import RecycleBoxLayout
from kivy.uix.recycleview import RecycleView
from kivy.uix.recycleview.layout import LayoutSelectionBehavior
from kivy.uix.recycleview.views import RecycleDataViewBehavior

import machines
from machines import Machine

Builder.load_file('predixio_widgets/recyclerview.kv')

class SelectableRecycleBoxLayout(FocusBehavior, LayoutSelectionBehavior,
                                 RecycleBoxLayout):
    ''' Adds selection and focus behaviour to the view. '''


###Machine
class RecycleMachines(RecycleView):
    def __init__(self, **kwargs):
        super(RecycleMachines, self).__init__(**kwargs)
        self.data = machines.load_machines()
        # self.data = [{'text': str(x)} for x in range(100)]


class SelectableLabelMachine(RecycleDataViewBehavior, Label):
    ''' Add selection support to the Label '''
    index = None
    selected = BooleanProperty(False)
    selectable = BooleanProperty(True)

    def refresh_view_attrs(self, rv, index, data):
        ''' Catch and handle the view changes '''
        self.index = index
        return super(SelectableLabelMachine, self).refresh_view_attrs(
            rv, index, data)

    def on_touch_down(self, touch):
        ''' Add selection on touch down '''
        if super(SelectableLabelMachine, self).on_touch_down(touch):
            return True
        if self.collide_point(*touch.pos) and self.selectable:
            return self.parent.select_with_touch(self.index, touch)

    def apply_selection(self, rv, index, is_selected):
        ''' Respond to the selection of items in the view. '''
        self.selected = is_selected
        if is_selected:
            app = App.get_running_app()
            machine_name = rv.data[index].get('text')
            app.variables.update({'machine': machine_name})
            machine = Machine(machine_name)
            material_list = machine.get_material_list()
            app.screen_manager.get_screen('first_screen').ids.recycle_material_piece.data = material_list
            app.screen_manager.get_screen('first_screen').ids.recycle_material_support.data = material_list
            app.machine = rv.data[index].get('text')
        else:
            print("selection removed for {0}".format(rv.data[index]))


###Material
class RecycleMaterial(RecycleView):
    def __init__(self, **kwargs):
        super(RecycleMaterial, self).__init__(**kwargs)
        self.data = []
        self.id = "material"


class SelectableLabelMaterial(RecycleDataViewBehavior, Label):
    ''' Add selection support to the Label '''
    index = None
    selected = BooleanProperty(False)
    selectable = BooleanProperty(True)

    def refresh_view_attrs(self, rv, index, data):
        ''' Catch and handle the view changes '''
        self.index = index
        return super(SelectableLabelMaterial, self).refresh_view_attrs(
            rv, index, data)

    def on_touch_down(self, touch):
        ''' Add selection on touch down '''
        if super(SelectableLabelMaterial, self).on_touch_down(touch):
            return True
        if self.collide_point(*touch.pos) and self.selectable:
            return self.parent.select_with_touch(self.index, touch)

    def apply_selection(self, rv, index, is_selected):
        ''' Respond to the selection of items in the view. '''
        self.selected = is_selected
        if is_selected:
           # print("selection changed to {0}".format(rv.data[index]))
            app = App.get_running_app()
            material = rv.data[index].get("text")
            if rv.a:
                app.variables.update({'materiau_piece': material})
            else:
                app.variables.update({'materiau_support': material})

        else:
            #print("selection removed for {0}".format(rv.data[index]))
            pass


###Couples
class RecycleCouple(RecycleView):
    def __init__(self, **kwargs):
        super(RecycleCouple, self).__init__(**kwargs)
        self.data = []


class SelectableLabelCouple(RecycleDataViewBehavior, Label):
    ''' Add selection support to the Label '''
    index = None
    selected = BooleanProperty(False)
    selectable = BooleanProperty(True)

    def refresh_view_attrs(self, rv, index, data):
        ''' Catch and handle the view changes '''
        self.index = index
        return super(SelectableLabelCouple, self).refresh_view_attrs(
            rv, index, data)

    def on_touch_down(self, touch):
        ''' Add selection on touch down '''
        if super(SelectableLabelCouple, self).on_touch_down(touch):
            return True
        if self.collide_point(*touch.pos) and self.selectable:
            return self.parent.select_with_touch(self.index, touch)

    def apply_selection(self, rv, index, is_selected):
        ''' Respond to the selection of items in the view. '''
        self.selected = is_selected
        if is_selected:
            App.get_running_app().index = index
        else:
            pass
            #print("selection removed for {0}".format(rv.data[index]))
