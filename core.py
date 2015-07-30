#!/usr/bin/env python
# -*- coding: utf-8 -*-


import iodata


class Core:
	def __init__(self):

		# Liste des Tabs
		# self.tablist = [[tab], [tab], ..., [tab]]
		# Avec:
		# [tab] = ["title", [fond d'écran],
		#			[iconsList]]
		# [fond d'écran] = ["color", "pathname image"]
		# [iconsList] = [[icon], [icon], ... [icon]]
		# [icon] = ["title", [fond], (position),
		#			[links]]
		# [fond] = ["bg color", "pathname_image"]
		#
		# (position) = Exemple (600, 300)
		# [links] = [link1, link2, ... link5]
		

		self.tablist = []
		
		# Import du tablist stocké
		var = iodata.manage_data((1, "./data/datafile.py"))
		if var[0] == True:
			self.tablist = var[1]
		else:
			pass
	
		
		
	def search_tab(self, title):
		# Retourne (Tab, index du tab) si le tab dont le titre
		# est donné existe sinon retourne False.

		# Cherche dans le tablist
		index = None
		for tab in self.tablist:
			title_tab = tab[0]
			if title_tab.lower() == title.lower():
				index = self.tablist.index(tab)
				break
			
		if index == None:
			return False
		else:
			return (tab, index)
		
		

		
	def next_tab(self, current_title, move = "next"):
		# Retourne le tab qui suit ou qui précede
		# (dépendamment de l'argument MOVE) celui dont le 
		# title est inscrit dans current_title
		
		# - current_title contient le nom du tab courant
		# - Le parametre move prend les valeurs
		#		next ou prev.
		
		# Lorsque "prev" ou "next" est choisi pour move,
		#	la fonction renvoie le tab précédent ou suivant
		#	celui dont le title est donné.
		# Lorsque le tab demandé n'existe pas, alors la
		# 	fonction renvoie False
		# Lorsque title est None, alors la fonction renvoie
		#	le premier tab dans le tablist, sinon return False
		#	si le tablist est vide
		
		# Return un tab, sinon return False
		
		
		
		if current_title == None:
			try:
				tab = self.tablist[0]
			except:
				return False
			else:
				return tab
		
		else:	
				retour = self.search_tab(current_title)
				
				if retour ==  False:
					return False
				else:
					index = retour[1]
				# Next
				if move == "next":
					index += 1
				# Prev
				else:
					index -= 1
				
				try:
					tab = self.tablist[index] 
				except:
					try:
						tab = self.tablist[0]
					except:
						return False
					else:
						return tab
				else:
					return tab
	
	


	def create_tab(self, tab):

		# Creation de Tab
		# [tab] (Voir description dans __init__)
		# Retourne True si la création de Tab est effective
		# Retourne False si échec de création de Tab
		
		# Check si le nom de tab existe deja
		title_tab = tab[0]	
		retour = self.search_tab(title_tab)
		if retour == False:
			self.tablist.append(tab)
			#self.tablist.sort()
			# Stockage du tablist
			iodata.manage_data((0, "./data/datafile.py", self.tablist))
			
			return True
			
		else:
			return False


		
	def modif_tab(self, tab):
	
		# Renvoyer True si modification effective d'un tab existant
		# Renvoyer False sinon

		# Check si le nom de tab existe deja	
		title_tab = tab[0]
		retour = self.search_tab(title_tab)
		if retour == False:
			return False
		else:
			# Ancien tab
			old_tab = retour[0]
			# On efface l'ancien tab du tablist
			self.tablist.remove(old_tab)
			# On ajoute le nouveau Tab
			self.tablist.append(tab)
			#self.tablist.sort()
			# Stockage du tablist
			iodata.manage_data((0, "./data/datafile.py", self.tablist))
			
			return True
	
	
	
	def remove_tab(self, tab):
		# Retire le tab du tablist
		# Retourne True si bonne fin
		# Retourne False sinon
		
		try:
			self.tablist.remove(tab)
		except:
			return False
		else:
			# Stockage du tablist
			iodata.manage_data((0, "./data/datafile.py", self.tablist))

			return True
			
			
			
	def search_icon(self, tab_title, icon_title):
		# Retourne ([icon]) de l'icon dont le title
		# est donné sinon retourne False.

		# Cherche dans le tablist
		retour = self.search_tab(tab_title)
	
		if retour == False:
			
			return False
		else:
			tab = retour[0]
		
			bool = False
			for icon in tab[2]:
				if icon[0] == icon_title:
					bool = True
					break
			if bool == True:
				return icon
			else:
				return False
	

	
	def create_icon(self, tab_title, icon):
		# Return True si l'icon est créé, sinon return False
		
		icon_title = icon[0]
		retour = self.search_icon(tab_title, icon_title)
	
		if retour == False:
			retour = self.search_tab(tab_title)
			if retour == False:
				return False
			else:
				tab = retour[0]
				tab[2].append(icon)
				# Stockage du tablist
				iodata.manage_data((0, "./data/datafile.py", self.tablist))

				return True
		else:
			return False


			
	def modif_icon(self, tab_title, icon):
		# Return True si l'icon est modifié sinon return False
		icon_title = icon[0]
		retour = self.search_icon(tab_title, icon_title)
	
		if retour == False:
			return False
			
		else:
			old_icon = retour
			retour = self.search_tab(tab_title)
			tab = retour[0]
			tab[2].remove(old_icon)
			tab[2].append(icon)
			# Stockage du tablist
			iodata.manage_data((0, "./data/datafile.py", self.tablist))

			return True


			
	def remove_icon(self, tab_title, icon):
		# Return True si l'icon est effacé sinon return False
		icon_title = icon[0]
		retour = self.search_icon(tab_title, icon_title)
	
		if retour == False:
			return False
			
		else:
			retour = self.search_tab(tab_title)
			tab = retour[0]
			tab[2].remove(icon)
			# Stockage du tablist
			iodata.manage_data((0, "./data/datafile.py", self.tablist))

			return True
			