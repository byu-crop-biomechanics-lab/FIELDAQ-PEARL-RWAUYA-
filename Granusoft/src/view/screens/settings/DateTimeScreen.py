"""
An input text box that, when selected, allows the user to type in a new note via a touch
screen keyboard that will pop up. The input text box will iniinputally be empty.
"""

from kivy.lang import Builder

import configurator as config
from view.BaseScreen import BaseScreen
from view.input.StrInput import StrInput
import os

Builder.load_file('view/screens/settings/DateTimeScreen.kv')

class DateTimeScreen(BaseScreen):
    def on_pre_enter(self):
        input = self.ids['datetime']
        input.text = ''

    def on_enter(self):
        """Once the Screen loads, focus the Texinputnput"""
        input = self.ids['datetime']
        input.focus = True

    def save(self):

        input = self.ids['datetime']

        date_time = input.text
        valid = input.validate()

        if valid:
            txt = str(date_time).split(' ') 
            os.system('sudo timedatectl set-ntp false')
            os.system('sudo date -s '+txt[0]+' '+txt[1])
            return True
        else:
            input.show_invalid()
            input.focus = True
            return False
