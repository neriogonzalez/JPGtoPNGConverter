import sys
import os

from PIL import Image

# 1.- use sys to grab first and second argumatn
dir1 = sys.argv[1]
dir2 = sys.argv[2]

# 2.- Verifica y crea el directorio de destino
if not os.path.exists(dir2):
    os.mkdir(dir2)

# 3.- loop into pokedex, convert images, move to new folder
for file_name in os.listdir(dir1):
    img = Image.open(f'{dir1}{file_name}')
    nuevo_nombre = os.path.splitext(file_name)
    img.save(f'{dir2}{nuevo_nombre[0]}.png', 'PNG')
    print(f'All done')
