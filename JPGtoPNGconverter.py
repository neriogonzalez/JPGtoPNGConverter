import sys
import os
import re
from PIL import Image


# Expresión regular

# re para directorio windows ^[a-zA-Z]:\\[\\\S|*\S]?.*$
pattern = re.compiler(r"[A-Z a-z 0-9 #$@%]{8,}\d")

string = "super$secret1@%#$2"

a = pattern.fullsearch(string)qq
print(a)

# Fin de Expresión regular

# agregando un comentario2
# grab first and  second argument
param = input('Ingresa directorios a utilizar: ')
b = 0


# check if new existe, if not create it

 try:
        # Create target Directory
        os.mkdir(dirName)
        print("Directory ", dirName,  " Created ")
    except FileExistsError:
        print("Directory " , dirName ,  " already exists")        
    
    # Create target Directory if don't exist
    if not os.path.exists(dirName):
        os.mkdir(dirName)
        print("Directory " , dirName ,  " Created ")
    else:    
        print("Directory " , dirName ,  " already exists")


#    loop on pokedex 

# conver image to png

# save to the new folder
