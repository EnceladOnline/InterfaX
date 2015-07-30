# Contient du script pour faire apparaitre des popup

from tkinter import filedialog
from tkinter import colorchooser
from tkinter import messagebox
import os.path


def filedialog_file(initial_dir, filetypes = [("All files", "*.*")]):
	# Permet de naviguer dans les repertoires pour choisir
	# des fichiers et recevoir leurs filenames
	# Dir est le pathname du dossier initial
	# Return le path name du fichier choisi
	# Sinon return "." si annulation
	
	filename = filedialog.askopenfilename(title = "Choose a file",
			filetypes = filetypes,
			initialdir = initial_dir)
			
	return os.path.normpath(filename)

	
	
def filedialog_dir(initial_dir):
	# Permet de naviguer dans les dossiers pour en
	# choisir un
	# Dir est le pathname du dossier initial
	# Return le pathname du dossier choisi
	# Sinon return "." si annulation
	
	dirname = filedialog.askdirectory(title = "Choose a directory",
			 initialdir = dir)
			
	return os.path.normpath(dirname)
	
	
def colorchooser_func():
	# Choisir une couleur depuis un pop up sympa
	# Annuler: return (None, None)
	
	color = colorchooser.askcolor(color = "red")
	
	return color
	
	
def confirm(msg):
	# Demande confirmation pour executer une opération
	# Dir est le message à afficher
	# Return True ou False
	
	retour = messagebox.askyesno(message = msg, icon = "warning")
	
	return retour
	

def info(msg):
	# Affiche une information
	# Msg est l'info en question
	
	messagebox.showinfo(message = msg)

	
#input(colorchooser_func())