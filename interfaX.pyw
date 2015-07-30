#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
    InterfaX - a task oriented desktop - Version 1.0.1
   
    Copyright (C) 2015 EnceladOnline

    This program is free software; you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation; either version 2 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program; if not, write to the Free Software
    Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA

"""



import os
import time
from tkinter import *
from tkinter import ttk

import tab
import core
import drag
import popup
import thumb
import toplevelF


	

class Graphic(Tk):
	def __init__(self):
		Tk.__init__(self)
		""" Cette classe contient le root de toute l'interface
		graphique. Elle pourvoit l'objet self.frame pour les
		besoins d'édition du widget tab.
		
		Utilisation:
			interfaX = Graphic()
			interfax.graphique() # Charge le graphique minimal
			interfax.load_tab() """
	
		# Instanciation ...
		self.core = core.Core()
		
		# Copie de la tablist
		self.copy_tablist = self.core.tablist.copy()
		
		# Dico pour stocker les ref des objets tab créés
		# y compris les objets icon créés afin de pouvoir
		# y appliquer .destroy()
		
		# self.tab_loaded = ["title tab", obj, [[icon], [icon],..]]
		# Avec icon = ["title icon", obj, [[tab link],
		# 			[link], [link] ...]
		self.tab_loaded = None
		
		# Les StringVar du graphique de base
		self.strvar_tab_title = StringVar()
		self.strvar_icon_title = StringVar()

		# Cache utile pour tous les objets qui communique avec Graphic
		self.cache = dict()

		self.cache["CurrentTab"] = None # List
		self.cache["CurrentTabID"] = None # Obj canvas (tab)
		
		self.cache["CurrentIcon"] = None # List
		self.cache["CurrentIconID"] = None # Obj Button (icon)
		self.cache["CurrentIconTAGORID"] = None # Obj tagorid icon
		self.cache["CurrentIconPosition"] = None # cache position icon
		
		self.cache["CurrentToplevel"] = None # Obj toplevel
		
		self.cache["drag_bool"] = False
		
		
		
	def graphique(self):
		# Le graphique
		self.state("zoomed") # Permet d'avoir la surface utilisable de windows
		self.update() # Utile pour pouvoir get la taille rafraichie de l'écran
		self.width = self.winfo_width()
		self.height = self.winfo_height()
		self.configure(background = "white")
		
		var = str(self.width) + "x" + str(self.height)
		
		self.geometry(var)
		
		self.master_can = Canvas(self, width = self.width-5,
							height = self.height, bg = "white")
		self.master_can.pack()
			# Bind
		self.master_can.bind("<Button-3>", self.tab_menu_eventhandler)
			
			# Tab Title
		self.tab_title = ttk.Entry(self, font = ("Arial", 10, "bold"),
			textvariable = self.strvar_tab_title, width = 28)
			# Bind
		self.tab_title.bind("<Return>", self.search)
		
		self.master_can.create_window(0, 0, window = self.tab_title,
					anchor = "nw")

			# Icon Title
		icon_title = ttk.Entry(self, width = 28, font = ("Arial", 10, "bold"),
			textvariable = self.strvar_icon_title, state = DISABLED)
		
		self.master_can.create_window(self.width, 0, window = icon_title,
					anchor = "ne")

					

		# Style
		self.style = ttk.Style()
		self.style.configure("STYLE_A.TButton", font = ("Arial", 8, "bold"))
		self.style.configure("STYLE_B.TButton", font = ("Arial", 10, "bold"))
		
		# Prev Tab Button
		prev_button = ttk.Button(self, text = "Prev Tab", style = "STYLE_A.TButton",
					command = lambda : self.button_next_tab("prev"),
					takefocus = 0, cursor = "hand2")
		self.master_can.create_window(260, 0, window = prev_button,
					anchor = "nw")

		# Next Tab Button
		next_button = ttk.Button(self, text = "Next Tab", style = "STYLE_A.TButton",
					command = self.button_next_tab, takefocus = 0, cursor = "hand2")
		self.master_can.create_window(348, 0, window = next_button,
					anchor = "nw")
					
		# Edit this tab
		edit_button = ttk.Button(self, text = "Edit Tab", style = "STYLE_A.TButton",
					command = self.button_edit_tab, takefocus = 0, cursor = "hand2")
		self.master_can.create_window(436, 0, window = edit_button,
					anchor = "nw")
			
		# Create tab
		create_tab_button = ttk.Button(self, text = "Create Tab", style = "STYLE_A.TButton",
					command = self.button_make_tab, takefocus = 0, cursor = "hand2")
		self.master_can.create_window(524, 0, window = create_tab_button,
					anchor = "nw")			
		
		# Create Icon
		create_icon_button = ttk.Button(self, text = "Create Icon", style = "STYLE_A.TButton",
					command = self.button_make_icon, takefocus = 0, cursor = "hand2")
		self.master_can.create_window(612, 0, window = create_icon_button,
					anchor = "nw")	

		# Del this tab
		del_button = ttk.Button(self, text = "Del Tab", style = "STYLE_A.TButton",
					command = self.button_del_tab, takefocus = 0, cursor = "hand2")
		self.master_can.create_window(700, 0, window = del_button,
					anchor = "nw")

		
		# Help Button
		help_button = ttk.Button(self, text = "Help", style = "STYLE_A.TButton",
					command = self.help, takefocus = 0, cursor = "hand2")
		self.master_can.create_window(788, 0, window = help_button,
					anchor = "nw")


		
		# Nom de l'app
		self.master_can.create_text(876, 0, text = "INTERFAX",
				font = ("Freestyle Script", 15, "bold"), anchor = "nw", fill = "gray")
		
			
			# Tab Area Frame
		
		self.tab_height = self.height - 25
		self.frame = Frame(self, width = self.width, height = self.tab_height, bg = "yellow")
		self.frame.grid_propagate(0) # Forcer le frame a respecter sa taille
	
		x = self.width/2 + 1
		self.master_can.create_window(x, 25, window = self.frame,
						anchor = "n") 
				# Bind
		self.frame.bind("<Button-3>", self.tab_menu_eventhandler)
		self.bind("<Return>", self.stop_drag_func)
		

		
	def next_tab(self, move = "next"):
		# S'occupe du chargement du prochain tab ou du précedent
		# cela dépend de l'argument MOVE
		try:
			self.cache["CurrentToplevel"].destroy()
		except:
			pass		
		if self.cache["CurrentTab"] == None:
			retour = self.core.next_tab(None, move)
		else:
			retour = self.core.next_tab(self.cache["CurrentTab"][0], move)
			
		
		if retour == False:
			pass
		else:
			try:
				self.cache["CurrentTabID"].destroy()
			except:
				pass
			self.cache["CurrentTab"] = retour
			self.strvar_tab_title.set(self.cache["CurrentTab"][0])
			tab.TabMaker(self).install()	
		
		
		
	def this_tab(self, title):
		# S'occupe du chargement du tab dont le title est donné
		
	
		retour = self.core.search_tab(title)
		if retour == False:
			popup.info("This tab doesn't exist !")
		else:
			try:
				self.cache["CurrentTabID"].destroy()
			except:
				pass
			
			self.cache["CurrentTab"] = retour[0]
			self.strvar_tab_title.set(self.cache["CurrentTab"][0])
			tab.TabMaker(self).install()

			
	def search(self, event):
		if self.cache["drag_bool"] == False:
			title = self.strvar_tab_title.get()
			
			self.this_tab(title)
		
		
	def del_tab(self):
		
		# Efface le tab courant et le retire aussi du tablist
		retour = popup.confirm("Are you sure to remove this tab of InterfaX?")
		
		if retour == True:
			self.cache["CurrentTabID"].destroy()
			self.core.remove_tab(self.cache["CurrentTab"])
			self.cache["CurrentTab"] = None
			self.strvar_tab_title.set("")
			self.next_tab()
		else:
			pass
	
	
	def del_icon(self):
		# Efface l'icon visé et le retire aussi du tablist
		retour = popup.confirm("Are you sure to remove this Icon of InterfaX?")
		if retour == True:
			self.cache["CurrentIconID"].destroy()
			self.core.remove_icon(self.cache["CurrentTab"][0],
						self.cache["CurrentIcon"])
		
		else:
			pass
	

		
	
	def tab_menu_eventhandler(self, event):
		# Commande pour faire apparaitre le menu de tab

		toplevelF.TabMenu(self)
	
	
	def icon_menu_eventhandler(self):
		# Commande pour faire apparaitre le menu d'icon

		toplevelF.IconMenu(self)
	
	
	
	def thumb_manager(self, type, pathname):
		# Permet de créer des miniatures au format .gif d'images
		#	.png, .jpg, et .gif
		
		# Type = "tab" ou "icon"
		# Pathname = "chemin de l'image"
		
		# Return le pathname complet du nouveau fichier gif
		# sinon return False
	
	
		if type == "tab":
			size = (self.width, self.tab_height)
			
			destination_pathname = "./tab_image"
			
			custom_name = str(int(time.time())) + ".gif"
			
			data = (pathname, destination_pathname, custom_name, "GIF",
						size)
			retour = thumb.resizer(data)
		
		else:
			size = (150, 150)
			
			destination_pathname = "./thumb"
			
			custom_name = str(int(time.time())) + ".gif"
			
			data = (pathname, destination_pathname, custom_name, "GIF",
						size)
			retour = thumb.thumbnail_maker(data)
	

		if retour == True:
			if type == "tab":
				return "./tab_image/" + custom_name 
			else:
				return "./thumb/" + custom_name 
		else:
			return False
	
	
	
	def drag_func(self):
		# S'occupe de faire glisser un icon sur le canvas
		# Permet ensuite d'enregistrer la nouvelle position de l'icon
		self.cache["drag_bool"] = True
		
	

	
	def stop_drag_func(self, event):
		
		if self.cache["drag_bool"] == True:	
			
			self.cache["drag_bool"] = False
			# On update
			self.cache["CurrentIcon"][2] = self.cache["CurrentIconPosition"]
			retour = self.core.modif_icon(self.cache["CurrentTab"][0],
					self.cache["CurrentIcon"])
			self.cache["CurrentIcon"] = None
		
		
	def drag_eventhandler(self, event):
	
		self.strvar_icon_title.set("")			
	
		if self.cache["drag_bool"] == True:
			drag.drag(self.cache["CurrentTabID"],
					self.cache["CurrentIconTAGORID"], event,
					self.func_get_position)	

	
	def func_get_position(self, position):
		self.cache["CurrentIconPosition"] = position
		
		
	def button_next_tab(self, move = "next"):
		self.next_tab(move)

		
	
	def button_edit_tab(self):
		if self.cache["CurrentTab"] == None:
			pass
		else:
			toplevelF.TabEditMenu(self, update = True)
	

	
	def button_make_tab(self):
		# Call TabEditMenu
		toplevelF.TabEditMenu(self)
	
	
	def button_make_icon(self):
		if self.cache["CurrentTab"] == None:
			pass
		else:
			# call icon maker
			toplevelF.IconEditMenu(self)
			
	
		
	def button_del_tab(self):
		if self.cache["CurrentTab"] == None:
			pass
		else:
			self.del_tab()
		
		
		
	def help(self):
		
		popup.info("InterfaX 1.0.1\nTask Oriented Desktop\nCreator: EnceladOnline\nContact: encelad.online@outlook.fr\nLicence: GNU GPL")
		
		try:
			os.system("start ./HELP.pdf")
		except:
			pass
		
		
		
interfax = Graphic()
interfax.graphique()
interfax.next_tab()

interfax.mainloop()