# Module contenant quelques fonctions utiles relatives au
# pathname

import os
import os.path


def pathfunc(path):
	# Return False si le path n'existe pas
	# Sinon return ("dir|file", parent)
	
	if os.path.exists(path):
		type = "file"
		if os.path.isdir(path):
			type = "dir"
		else:
			pass
		parent = os.path.dirname(path)
		return (type, parent)
	else:
		return False
		
		
def launcher(path_list):
	# Executer une liste de pathnames
	for path in path_list:
		try:
			if os.path.exists(path):
					os.startfile(path)
		except:
			pass
		else:
			pass

			
def homepath():
	# Retourne le pathname du profile utilisateur courant
	var = os.popen("set homepath").read()
	return "C:" + var.split("=")[1]
	