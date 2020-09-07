import sys
import os

from PIL import Image

# 1.- use sys to grab first and second argumatn
dir1 = sys.argv[1]
dir2 = sys.argv[2]
#print('directorio origen:' + dir1 + ', directorio destino:' + dir2)


# 2.- # check if exist, if not created new dir

#dir1 = '\\Pokedex'
#dir2 = '\\Nuevo\\'

var_path = (os.getcwd() + '\images\JPGtoPNGConverter')
dir1 = var_path + '\\' + dir1
dir2 = var_path + '\\' + dir2
print(f'dir1:  {dir1}')
print(f'dir2:  {dir2}')

os.chdir(var_path)


# files = [f for f in os.listdir('.') if os.path.isfile(f)]


if not os.path.exists(dir1):
    os.mkdir(dir1)

if not os.path.exists(dir2):
    os.mkdir(dir2)


# 3.- loop into pokedex, conver images, move to new folder
os.chdir(dir1)
for f in os.listdir(dir1):
    print('path: ' + os.getcwd())

    img = Image.open(f)
    nuevo_nombre = f[0: len(f) - 4:1]
    print(f'el nuev nombre es: {nuevo_nombre}')
    print(f'{f} + abierto')
    print(f'dir2: {dir2}')
    img.save(dir2+nuevo_nombre+'.png', 'PNG')
    print(f'{f} + salvado')
