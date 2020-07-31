import sys
import os
from PIL import Image
# agregando un comentario2
# grab first and  second argument
param = input('Ingresa directorios a utilizar: ')
a = 0


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
