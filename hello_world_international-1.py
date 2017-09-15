# Created by: Malcolm McCarthy
# Created on: Sept 2017
# Created for: ICS3U
# This program is the Hello, World program, but with 3 buttons

import ui

def  english_touch_up_inside(sender):
		 #displays the english vesion
		 view['hello_world_label'].text = ('Hello, World!')
		
def french_touch_up_inside(sender):
		#displays the french version
		view['hello_world_label'].text = ('Bonjour le monde!')

def spanish_touch_up_inside(sender):
	  #displays the spansish version
	  view['hello_world_label'].text = ('Hola Mundo!')
	  
view = ui.load_view()
view.present('sheet')
