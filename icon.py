from tkinter import *
from tkinter import ttk
import func

class Icon:
	def __init__(self, main, icon):
		# Affiche les icon sur le tab
		
		self.main = main
		
		self.master = self.main.cache["CurrentTabID"]
		
		self.icon = icon
		
		if self.icon[1][1] == None:
			self.icon_label()
		else:
			self.icon_image()
	
		
	def icon_label(self):
		
		self.cadre = ttk.Button(self.main.cache["CurrentTabID"],
				text = self.icon[0], command = self.launch,
				style = "STYLE_B.TButton", takefocus = 0, cursor = "hand2")
		
		
		self.icon_tagorid = self.main.cache["CurrentTabID"].create_window(self.icon[2][0],
				self.icon[2][1], window = self.cadre, anchor = "se")
				
		
		self.main.cache["CurrentIconID"] = self.cadre
		self.main.cache["CurrentIcon"] = self.icon		
		
		
		# Bind
		self.cadre.bind("<Button-3>", self.icon_menu_eventhandler)
		# Utilisé dans InterfaX 1
		# self.cadre.bind("<Motion>", self.icon_title_eventhandler)

		
	def icon_image(self):

		try:
			self.main.cache[self.icon[0]] = PhotoImage(file = self.icon[1][1])
		
		except:
			self.main.cache[self.icon[0]] = None
			
			
		self.cadre = ttk.Button(self.main.cache["CurrentTabID"],
				image = self.main.cache[self.icon[0]], takefocus = 0,
				command = self.launch, cursor = "hand2")

				
		self.icon_tagorid = self.main.cache["CurrentTabID"].create_window(self.icon[2][0],
			self.icon[2][1], window = self.cadre, anchor = "se")

			
			
		# Bind
		self.cadre.bind("<Button-3>", self.icon_menu_eventhandler)
		self.cadre.bind("<Motion>", self.icon_title_eventhandler)
	
		
	def launch(self):
		path_list = self.icon[3]
		
		func.launcher(path_list)

		
	def icon_menu_eventhandler(self, event):
		self.main.cache["CurrentIconID"] = self.cadre
		self.main.cache["CurrentIcon"] = self.icon		
		self.main.cache["CurrentIconTAGORID"] = self.icon_tagorid
		self.main.icon_menu_eventhandler()
		
		
	def icon_title_eventhandler(self, event):
		self.main.strvar_icon_title.set(self.icon[0])
	
	