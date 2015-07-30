# Fonction pour stocker des objets et les récuperer au besoin

import pickle



def manage_data(data):	
	# Prototype data:
	# 	Pour stocker un objet (Exporter):
	#	=====================
	#		data = (0, "file pathname", object)
	#
	#	La fonction retourne:
	#		Bonne fin: True
	#		Exception: False
	#
	#
	#	Pour récuperer un objet (Importer):
	#	=======================
	#		data = (1, "file pathname")
	#
	#	La fonction retourne:
	#		Bonne fin: (True, objet)
	#		Exception: (False,)
	
	
	if data[0] == 0: # Exporter les données
		try:
			with open(data[1], "wb") as file:
				var = pickle.Pickler(file)
				var.dump(data[2])
		except:
			return False
		else:
			return True
			
	else: # Importer les données
		try:
			with open(data[1], "rb") as file:
				var = pickle.Unpickler(file)
				retour = var.load()
		except:
			return (False,)
		else:
			return (True, retour)

