# Code pour créer des miniatures et redimensionner les images

from PIL import Image as PIL_IMAGE

# Thanks to PIL


def thumbnail_maker(data):
	""" Createur de miniatures
	
	Prototype data = (file, "destination pathname",
				"customfilename", format, size)
	 -File est le pathname complet du file d'origine
	 -Le destination pathname ne doit pas avoir un slash final
		donc il doit être du style "c:/dir" et non pas "c:/dir/"
	 -Le customfilename est juste le nouveau nom du fichier, pas de
		slash.
	 -format = "GIF", "JPEG" ...
	 -example size = (40, 40)
	
	 Return True si bonne fin
	 Return FileError si le fichier n'a pas pu être ouvert
	 Return DestinationPathError """
	
	file = data[0]
	destination_pathname = data[1]
	custom_filename = data[2]
	format = data[3]
	size = data[4]
	
	try:
		image = PIL_IMAGE.open(file)
	except:
		return "FileError"
	else:
		try:
			image.thumbnail(size)
			image.save(destination_pathname + "/" + custom_filename, format)
		except:
			return "DestinationPathError"
		else:
			return True
			
		

		
def resizer(data):
	""" Modifie le size des images selon les dimensions données.
	
	Prototype data = (file, "destination pathname",
				"customfilename", format, size)
	 -File est le pathname complet du file d'origine
	 -Le destination pathname ne doit pas avoir un slash final
		donc il doit être du style "c:/dir" et non pas "c:/dir/"
	 -Le customfilename est juste le nouveau nom du fichier, pas de
		slash. Donc un truc genre "file.jpg" pas de "/file.jpg"
	 -format = "GIF", "JPEG" ...
	 -example size = (40, 40)
	
	 Return True si bonne fin
	 Return FileError si le fichier n'a pas pu être ouvert
	 Return DestinationPathError """
	
	file = data[0]
	destination_pathname = data[1]
	custom_filename = data[2]
	format = data[3]
	size = data[4]
	
	try:
		image = PIL_IMAGE.open(file)
	except:
		return "FileError"
	else:
		try:
			img = image.resize(size)
			img.save(destination_pathname + "/" + custom_filename, format)
		except:
			return "DestinationPathError"
		else:
			return True


#thumbnail_maker(("./pic1.jpg", "./dir", "THUMB.gif", "GIF", (500, 500)))
#resizer(("./pic2.jpg", "./dir", "RESIZE.gif", "GIF", (500, 500)))
