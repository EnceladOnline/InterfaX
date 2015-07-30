from tkinter import *
import icon


class TabMaker:
	def __init__(self, main):
		# S'occupe de l'installation du tab sur le tab area
		
		self.main = main
		
		self.frame = main.frame
		
		self.cache = main.cache
		
		self.tab_title = self.cache["CurrentTab"][0]
		self.tab_bg_color = self.cache["CurrentTab"][1][0]
		self.tab_img_pathname = self.cache["CurrentTab"][1][1]
		self.icon_list = self.cache["CurrentTab"][2]
		
		# Emplacement dans le dico cache pour stocker PhotoImage
		self.cache["tab_img"] = None
		
		
		
	def install(self):
		# Installe le tab sur le frame du graphique
		
		width = self.main.width
		height = self.main.tab_height
		self.tab_loaded = Canvas(self.frame, width = width,
				height = height, bg = self.tab_bg_color)
				
		self.tab_loaded.pack()
				
		
		# Image de fond
		if self.tab_img_pathname != None:
			try:
				self.cache["tab_img"] = PhotoImage(file = self.tab_img_pathname)
			except:
				pass
			else:
				x, y = self.main.width / 2, self.main.tab_height / 2
				self.tab_loaded.create_image(x, y,
								image = self.cache["tab_img"])
		else:
			pass
		
		# Stocker l'ID du tab afin de pouvoir y appliquer
		# destroy() plus tard
		self.cache["CurrentTabID"] = self.tab_loaded
		
				# Bind
		self.tab_loaded.bind("<Button-3>", self.main.tab_menu_eventhandler)
		self.cache["CurrentTabID"].bind("<Motion>",
			self.main.drag_eventhandler)	
		
		
		
		# Appeler IconMaker
		self.icon_maker()
		
	def icon_maker(self):
		# Installe les icon sur le tab
		
		for x in self.icon_list:
			icon.Icon(self.main, x)
			
	