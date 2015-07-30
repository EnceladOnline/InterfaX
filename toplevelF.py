# TopLevel Frames regroupe du code pour
# afficher des frames toplevel comme les pop-up dialog, le
# colorchooser, etc


from tkinter import *
from tkinter import ttk
import popup
import func



class TabMenu:

	def __init__(self, main):
		# Frame menu qui apparait quand on fait un clic droit
		# sur l'espace vierge d'un tab ou quand on fait un
		# clic gauche sur un title
	
		# Parameters:
		# ==========
		# master = master graphique
		# gate = fonction à appeler pour renvoyer le choix du user
		# 
		self.main = main
		
		self.master = main.frame

		try:
			self.main.cache["CurrentToplevel"].destroy()
		except:
			pass

		
		self.graphique()
		
		
		
	def graphique(self):
		
		self.toplevel = Toplevel(self.main)
		
		var = "180x160-" + str( int(self.main.width/2)) + "-" + str(int(self.main.height/2))
		self.toplevel.geometry(var)
		self.toplevel.title("Tab Menu")
		self.toplevel.resizable(0, 0)
		# Stockage du ID dans le cache
		self.main.cache["CurrentToplevel"] = self.toplevel
		
		canvas = Canvas(self.toplevel, width = 180, height = 160)
		canvas.pack()
		
		
		b1 = ttk.Button(self.toplevel, text = "Create New Icon", width = 20,
					command = self.make_icon)
		b2 = ttk.Button(self.toplevel, text = "Create New Tab", width = 20,
					command = self.make_tab)
		b3 = ttk.Button(self.toplevel, text = "Edit this Tab", width = 20,
					command = self.edit_tab)
		b4 = ttk.Button(self.toplevel, text = "Delete this Tab", width = 20,
					command = self.del_tab)
		
		
		canvas.create_window(5, 20, window = b1, anchor = "w")
		canvas.create_window(5, 60, window = b2, anchor = "w")
		canvas.create_window(5, 100, window = b3, anchor = "w")
		canvas.create_window(5, 140, window = b4, anchor = "w")

		
		
		
	def make_icon(self):
		if self.main.cache["CurrentTab"] == None:
			pass
		else:
			# call icon maker
			IconEditMenu(self.main)
		
	def edit_tab(self):
		if self.main.cache["CurrentTab"] == None:
			pass
		else:
			TabEditMenu(self.main, update = True)
		
	def make_tab(self):
		# Call TabEditMenu
		TabEditMenu(self.main)
		
	def del_tab(self):
		if self.main.cache["CurrentTab"] == None:
			pass
		else:
			self.toplevel.destroy()
			self.main.del_tab()
		
		
	def help_menu(self):
		pass



class TabEditMenu:

	def __init__(self, main, update = False):
		# Frame pour gerer la creation d'un nouveau tab
		# ou pour modifier un ancien tab
		
		# Parameters:
		# ==========
		# Main est la classe mère
		# update est mis à True si on veut editer/modifier un
		#   tab existant.
		# update est mis à False si on veut créer un nouveau tab
	
		# Detruire le toplevel qui serait là
		try:
			main.cache["CurrentToplevel"].destroy()
		except:
			pass

		self.main = main
		self.update = update
		self.master = main.frame
		
		self.strvar_title = StringVar()
		self.strvar_color = StringVar()
		self.strvar_image = StringVar()
		
		
		if self.update == True:
			var_title = self.main.cache["CurrentTab"][0]
			var_color = self.main.cache["CurrentTab"][1][0]
			var_image = self.main.cache["CurrentTab"][1][1]
			
			if var_title != None:
				self.strvar_title.set(var_title)
			if var_color != None:
				self.strvar_color.set(var_color)
			if var_image != None:
				self.strvar_image.set(var_image)
				
		self.graphique()
		
	
	
	def graphique(self):
	
		self.toplevel = Toplevel(self.master)
		
		var = "360x160-" + str( int(self.main.width/2)) + "-" + str(int(self.main.height/2))
		self.toplevel.geometry(var)
		self.toplevel.title("Edit Tab Menu")
		self.toplevel.resizable(0, 0)
		self.main.cache["CurrentToplevel"] = self.toplevel
		
		canvas = Canvas(self.toplevel, width = 360, height = 160)
		canvas.pack()
		
		label_title = Label(self.toplevel, text = "Title",
			font = ("Arial", 11))
		entry_title = ttk.Entry(self.toplevel, textvariable = self.strvar_title)
		
		label_color = Label(self.toplevel, text = "Color",
			font = ("Arial", 11))
		entry_color = ttk.Entry(self.toplevel, textvariable = self.strvar_color,
				state = DISABLED)
		button_color = ttk.Button(self.toplevel, text = "Choose",
				command = self.browse_color)
		
		label_image = Label(self.toplevel, text = "Image",
			font = ("Arial", 11))
		entry_image = ttk.Entry(self.toplevel, textvariable = self.strvar_image)
		button_image = ttk.Button(self.toplevel, text = "Browse",
					command = self.browse_image)

		
		button_save = ttk.Button(self.toplevel, text = "Save",
					command = self.save)
		
		button_cancel = ttk.Button(self.toplevel, text = "Cancel",
					command = self.cancel)
		

		
		# Ajout des titles sur le canvas
		canvas.create_window(5, 17, window = label_title, anchor = "w")
		canvas.create_window(5, 50, window = label_color, anchor = "w")
		canvas.create_window(5, 83, window = label_image, anchor = "w")
		
		# Ajout des entry sur le canvas
		canvas.create_window(90, 17, window = entry_title, anchor = "w")
		canvas.create_window(90, 50, window = entry_color, anchor = "w")
		canvas.create_window(90, 83, window = entry_image, anchor = "w")
		
		# Ajout des buttons sur le canvas
		canvas.create_window(260, 50, window = button_color, anchor = "w")
		canvas.create_window(260, 83, window = button_image, anchor = "w")
			
		canvas.create_window(90, 140, window = button_save, anchor = "w")
			
		canvas.create_window(190, 140, window = button_cancel, anchor = "w")

		# On ne modifie plus le title du tab
		if self.update == True:
			entry_title["state"] = DISABLED
	
	
	
	def browse_color(self):
		
		retour = popup.colorchooser_func()
		
		self.toplevel.focus_force()
		
		if retour == (None, None):
			pass
		else:
			self.strvar_color.set(retour[1])
		
		
	def browse_image(self):
		
		retour = popup.filedialog_file(initial_dir = "./image",
					filetypes = [("Image", ("*.jpg", "*.jpeg", "*.png", "*.gif", "*.bmp"))])
		
		self.toplevel.focus_force()
		
		if retour == ".":
			pass
		else:
			retour = self.main.thumb_manager("tab", retour)	
			if retour == False:
				pass
			else:
				self.strvar_image.set(retour)
		
		
		
	def save(self):
		
		title = self.strvar_title.get()
		new_color = self.strvar_color.get()
		new_image = self.strvar_image.get()
		
		if new_color == "":
			new_color = None
		if new_image == "":
			new_image = None
		
		
		# Edit
		if self.update == True:
			
			retour = popup.confirm("Are you sure to save new settings for this tab ?")
			
			
			if retour == True:
				icon_list = self.main.cache["CurrentTab"][2]
		
				modif_tab = [title, [new_color, new_image], icon_list] 
		
				retour = self.main.core.modif_tab(modif_tab)
				if retour == True:
					popup.info("Tab successfully modified")
					self.main.this_tab(title)
				else:
					popup.info("Error. Tab not modified")
				
			else:
				self.toplevel.focus_force()
				pass
		# Making new tab
		else:
				
			new_tab = [title, [new_color, new_image], []] 
			
			retour = self.main.core.create_tab(new_tab)
			
			if retour == True:
				popup.info("Tab successfully created")
				self.main.this_tab(title)
			else:
				popup.info("Error. Tab not created. Title already used")

		
		self.toplevel.destroy()
		
		
	def cancel(self):
		self.toplevel.destroy()


		
class IconMenu:
	def __init__(self, main):
		# Frame menu qui apparait quand on fait un clic droit
		# sur un icon

		# Parameters:
		# ==========
		# main
		
		self.main = main
		
		self.master = main.frame

		try:
			self.main.cache["CurrentToplevel"].destroy()
		except:
			pass

		
		self.graphique()
	

	def graphique(self):
		
		self.toplevel = Toplevel(self.main)
		var = "180x240-" + str( int(self.main.width/2)) + "-" + str(int(self.main.height/2))
		self.toplevel.geometry(var)
		self.toplevel.title("Tab Menu")
		self.toplevel.resizable(0, 0)		

		# Stockage du ID dans le cache
		self.main.cache["CurrentToplevel"] = self.toplevel

		canvas = Canvas(self.toplevel, width = 180, height = 240)
		canvas.pack()
		
		
		b1 = ttk.Button(self.toplevel, text = "Drag", width = 20,
				command = self.drag_icon)
		b2 = ttk.Button(self.toplevel, text = "Edit this Icon", width = 20,
				command = self.edit_icon)
		b3 = ttk.Button(self.toplevel, text = "Create New Icon", width = 20,
				command = self.make_icon)
		b4 = ttk.Button(self.toplevel, text = "Create New Tab", width = 20,
				command = self.make_tab)
		b5 = ttk.Button(self.toplevel, text = "Del this Tab", width = 20,
				command = self.del_tab)
		b6 = ttk.Button(self.toplevel, text = "Del this Icon", width = 20,
				command = self.del_icon)
		
		
		
		canvas.create_window(5, 20, window = b1, anchor = "w")
		canvas.create_window(5, 60, window = b2, anchor = "w")
		canvas.create_window(5, 100, window = b3, anchor = "w")
		canvas.create_window(5, 140, window = b4, anchor = "w")
		canvas.create_window(5, 180, window = b5, anchor = "w")
		canvas.create_window(5, 220, window = b6, anchor = "w")
		
	
	
	def make_icon(self):
		if self.main.cache["CurrentTab"] == None: # On ne crée d'icon que sur un tab qui existe
			pass
		else:
			self.toplevel.destroy()
			# call icon edit menu
			IconEditMenu(self.main)
		
		
	def edit_icon(self):
		self.toplevel.destroy()
		# call icon edit menu
		IconEditMenu(self.main, update = True)		
		

	def make_tab(self):
		self.toplevel.destroy()
		# Call TabEditMenu
		TabEditMenu(self.main)
		
		
	def del_icon(self):
		
		self.toplevel.destroy()
		self.main.del_icon()

		
	def del_tab(self):
		self.toplevel.destroy()
		self.main.del_tab()

		
	def drag_icon(self):
		self.toplevel.destroy()
		self.main.drag_func()

		
		
		
		
		
class IconEditMenu:
	
	def __init__(self, main, update = False):
	
		# Frame pour gerer la creation d'un nouveau icon
		# ou pour modifier un ancien icon
		
		# Parameters:
		# ==========
		# Main est la classe mère
		# update est mis à True si on veut editer/modifier un
		#   icon existant.
		# update est mis à False si on veut créer un nouveau icon
	
		# Detruire le toplevel qui serait là
		try:
			main.cache["CurrentToplevel"].destroy()
		except:
			pass

		self.main = main
		self.update = update
		self.master = main.frame
		
		self.strvar_title = StringVar()
		self.strvar_color = StringVar()
		self.strvar_image = StringVar()
		self.strvar_link1 = StringVar()
		self.strvar_link2 = StringVar()
		self.strvar_link3 = StringVar()
		self.strvar_link4 = StringVar()
		self.strvar_link5 = StringVar()
		
		if self.update == True:
			
			var_title = self.main.cache["CurrentIcon"][0]
			var_color = self.main.cache["CurrentIcon"][1][0]
			var_image = self.main.cache["CurrentIcon"][1][1]
			
			var_link1 = self.main.cache["CurrentIcon"][3][0]
			var_link2 = self.main.cache["CurrentIcon"][3][1]
			var_link3 = self.main.cache["CurrentIcon"][3][2]
			var_link4 = self.main.cache["CurrentIcon"][3][3]
			var_link5 = self.main.cache["CurrentIcon"][3][4]
			
			if var_title != None:
				self.strvar_title.set(var_title)
			if var_color != None:
				self.strvar_color.set(var_color)
			if var_image != None:
				self.strvar_image.set(var_image)
			if var_link1 != None:
				self.strvar_link1.set(var_link1)
			if var_link2 != None:
				self.strvar_link2.set(var_link2)
			if var_link3 != None:
				self.strvar_link3.set(var_link3)
			if var_link4 != None:
				self.strvar_link4.set(var_link4)
			if var_link5 != None:
				self.strvar_link5.set(var_link5)
				
				
		self.graphique()



	def graphique(self):
	
		self.toplevel = Toplevel(self.master)

		var = "375x345-" + str( int(self.main.width/2)) + "-" + str(int(self.main.height/2))
		self.toplevel.geometry(var)
		self.toplevel.title("Edit Icon Menu")
		self.toplevel.resizable(0, 0)
		self.main.cache["CurrentToplevel"] = self.toplevel

		canvas = Canvas(self.toplevel, width = 375, height = 345)
		canvas.pack()
		
		label_title = Label(self.toplevel, text = "Title:",
			font = ("Arial", 11))
		entry_title = ttk.Entry(self.toplevel, textvariable = self.strvar_title)
		
		label_color = Label(self.toplevel, text = "Color:",
			font = ("Arial", 11))
		entry_color = ttk.Entry(self.toplevel, textvariable = self.strvar_color)
		button_color = ttk.Button(self.toplevel, text = "Choose",
				command = self.browse_color)
		
		label_image = Label(self.toplevel, text = "Image:",
			font = ("Arial", 11))
		entry_image = ttk.Entry(self.toplevel, textvariable = self.strvar_image)
		button_image = ttk.Button(self.toplevel, text = "Browse",
				command = self.browse_image)

		
		label_link_1 = Label(self.toplevel, text = "Link_1:",
			font = ("Arial", 11))
		entry_link_1 = ttk.Entry(self.toplevel, textvariable = self.strvar_link1)
		button_dir_link_1 = ttk.Button(self.toplevel, text = "dir", width = 5,
				command = lambda : self.browse_file(1, type = "dir"))
		button_file_link_1 = ttk.Button(self.toplevel, text = "file", width = 5,
				command = lambda : self.browse_file(1, type = "file"))
		
		label_link_2 = Label(self.toplevel, text = "Link_2:",
			font = ("Arial", 11))
		entry_link_2 = ttk.Entry(self.toplevel, textvariable = self.strvar_link2)
		button_dir_link_2 = ttk.Button(self.toplevel, text = "dir", width = 5,
				command = lambda : self.browse_file(2, type = "dir"))
		button_file_link_2 = ttk.Button(self.toplevel, text = "file", width = 5,
				command = lambda : self.browse_file(2, type = "file"))
		

		label_link_3 = Label(self.toplevel, text = "Link_3:",
			font = ("Arial", 11))
		entry_link_3 = ttk.Entry(self.toplevel, textvariable = self.strvar_link3)
		button_dir_link_3 = ttk.Button(self.toplevel, text = "dir", width = 5,
				command = lambda : self.browse_file(3, type = "dir"))
		button_file_link_3 = ttk.Button(self.toplevel, text = "file", width = 5,
				command = lambda : self.browse_file(3, type = "file"))
		
		label_link_4 = Label(self.toplevel, text = "Link_4:",
			font = ("Arial", 11))
		entry_link_4 = ttk.Entry(self.toplevel, textvariable = self.strvar_link4)
		button_dir_link_4 = ttk.Button(self.toplevel, text = "dir", width = 5,
				command = lambda : self.browse_file(4, type = "dir"))
		button_file_link_4 = ttk.Button(self.toplevel, text = "file", width = 5,
				command = lambda : self.browse_file(4, type = "file"))
		
		label_link_5 = Label(self.toplevel, text = "Link_5:",
			font = ("Arial", 11))
		entry_link_5 = ttk.Entry(self.toplevel, textvariable = self.strvar_link5)
		button_dir_link_5 = ttk.Button(self.toplevel, text = "dir", width = 5,
				command = lambda : self.browse_file(5, type = "dir"))
		button_file_link_5 = ttk.Button(self.toplevel, text = "file", width = 5,
				command = lambda : self.browse_file(5, type = "file"))
		
		button_save = ttk.Button(self.toplevel, text = "Save",
				command = self.save)
		button_cancel = ttk.Button(self.toplevel, text = "Cancel",
				command = self.cancel)

		
		# Ajout des titles sur le canvas
		canvas.create_window(5, 17, window = label_title, anchor = "w")
		canvas.create_window(5, 50, window = label_color, anchor = "w")
		canvas.create_window(5, 83, window = label_image, anchor = "w")
		canvas.create_window(5, 126, window = label_link_1, anchor = "w")
		canvas.create_window(5, 159, window = label_link_2, anchor = "w")
		canvas.create_window(5, 192, window = label_link_3, anchor = "w")
		canvas.create_window(5, 225, window = label_link_4, anchor = "w")
		canvas.create_window(5, 258, window = label_link_5, anchor = "w")

		
		# Ajout des entry sur le canvas
		canvas.create_window(90, 17, window = entry_title, anchor = "w")
		canvas.create_window(90, 50, window = entry_color, anchor = "w")
		canvas.create_window(90, 83, window = entry_image, anchor = "w")
		canvas.create_window(90, 126, window = entry_link_1, anchor = "w")
		canvas.create_window(90, 159, window = entry_link_2, anchor = "w")
		canvas.create_window(90, 192, window = entry_link_3, anchor = "w")
		canvas.create_window(90, 225, window = entry_link_4, anchor = "w")
		canvas.create_window(90, 258, window = entry_link_5, anchor = "w")

		
		# Ajout des buttons sur le canvas
		canvas.create_window(260, 50, window = button_color, anchor = "w")
		canvas.create_window(260, 83, window = button_image, anchor = "w")
		canvas.create_window(260, 126, window = button_dir_link_1, anchor = "w")
		canvas.create_window(310, 126, window = button_file_link_1, anchor = "w")
		canvas.create_window(260, 159, window = button_dir_link_2, anchor = "w")
		canvas.create_window(310, 159, window = button_file_link_2, anchor = "w")
		canvas.create_window(260, 192, window = button_dir_link_3, anchor = "w")
		canvas.create_window(310, 192, window = button_file_link_3, anchor = "w")
		canvas.create_window(260, 225, window = button_dir_link_4, anchor = "w")
		canvas.create_window(310, 225, window = button_file_link_4, anchor = "w")
		canvas.create_window(260, 258, window = button_dir_link_5, anchor = "w")
		canvas.create_window(310, 258, window = button_file_link_5, anchor = "w")
		
		canvas.create_window(90, 320, window = button_save, anchor = "w")
		canvas.create_window(190, 320, window = button_cancel, anchor = "w")


		# On ne modifie plus le title du tab
		if self.update == True:
			entry_title["state"] = DISABLED
	
		

	def browse_color(self):
		
		retour = popup.colorchooser_func()
		
		self.toplevel.focus_force()
		
		if retour == (None, None):
			pass
		else:
			self.strvar_color.set(retour[1])
		
		
	def browse_image(self):
		
		retour = popup.filedialog_file(initial_dir = "./image", 
				filetypes = [("Image", ("*.jpg", "*.jpeg", "*.png", "*.gif", "*.bmp"))])
		
		self.toplevel.focus_force()
		
		if retour == ".":
			pass
		else:
			retour = self.main.thumb_manager("icon", retour)	
			if retour == False:
				pass
			else:
				self.strvar_image.set(retour)
		
	
	def browse_file(self, button, type = "file"):
		# Button est le numero du bouton
		# Le type permet définir le type de data à browser,
		# donc on a deux types: "file" et "dir"
		
		homepath = func.homepath()
		
		if type == "file":
			retour = popup.filedialog_file(initial_dir = homepath)
		else:
			retour = popup.filedialog_dir(initial_dir = homepath)
		
		self.toplevel.focus_force()
		
		if retour == ".":
			pass
		else:
			if button == 1:	
				self.strvar_link1.set(retour)
			elif button == 2:	
				self.strvar_link2.set(retour)
			elif button == 3:	
				self.strvar_link3.set(retour)
			elif button == 4:	
				self.strvar_link4.set(retour)
			elif button == 5:	
				self.strvar_link5.set(retour)

			
			
	def save(self):
		
		tab_title = self.main.cache["CurrentTab"][0]
		
		title = self.strvar_title.get()
		new_color = self.strvar_color.get()
		new_image = self.strvar_image.get()
		
		new_link1 = self.strvar_link1.get()
		new_link2 = self.strvar_link2.get()
		new_link3 = self.strvar_link3.get()
		new_link4 = self.strvar_link4.get()
		new_link5 = self.strvar_link5.get()
		
		
		if new_color == "":
			new_color = None
		if new_image == "":
			new_image = None
		if new_link1 == "":
			new_link1 = None
		if new_link2 == "":
			new_link2 = None
		if new_link3 == "":
			new_link3 = None
		if new_link4 == "":
			new_link4 = None
		if new_link5 == "":
			new_link5 = None
		
		
		
		# Edit
		if self.update == True:
			retour = popup.confirm("Are you sure to save new settings for this tab ?")
			
			
			if retour == True:
		
				position = self.main.cache["CurrentIcon"][2]
				modif_icon = [title, [new_color, new_image], position, 
						[new_link1, new_link2, new_link3, new_link4,
						new_link5]] 
		
				retour = self.main.core.modif_icon(tab_title, modif_icon)
				if retour == True:
					popup.info("Tab successfully modified")
					self.main.this_tab(tab_title)
				else:
					popup.info("Error. Tab not modified")
				
			else:
				self.toplevel.focus_force()
				pass
		# Making new Icon
		else:
				
			new_icon = [title, [new_color, new_image], (200, 200), 
						[new_link1, new_link2, new_link3, new_link4,
						new_link5]] 		
			retour = self.main.core.create_icon(tab_title, new_icon)
			
			if retour == True:
				popup.info("Icon successfully created")
				self.main.this_tab(tab_title)
			else:
				popup.info("Error. Icon not created. Title already used")

		
		self.toplevel.destroy()
			
			
			
			
			
	def cancel(self):
		self.toplevel.destroy()
	
		