# Func pour faire bouger en temps réel un widget sur un canvas
# au doigt et à l'oeil

from tkinter import *



def drag(canvas, widget, event, func_get_position):
	# Ceci update la position d'un widget
	# en fonction de celle du pointeur de la souris
	
	# Canvas = Le canvas sur lequel faire glisser le widget
	# Widget = TagOrID du widget installé sur le canvas
	# Rappelons qu'un tagOrID est comme ceci:
	# 		tagOrID = canvas.create_window(x, y, window = var)
	# event = objet event passé en parametre pour effectuer un bind
	# func_get_position = Renvoyer à cette fonction la position courante

	
	current_position_x = event.x
	current_position_y = event.y 
	
	canvas.coords(widget, current_position_x,
			current_position_y)
	
	func_get_position((current_position_x, current_position_y))