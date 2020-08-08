import os
import pathlib
import shutil
from PIL import Image

dir1 = r'\Pokedex'
dir2 = r'\Nuevo'
print(f'path inicial: {os.getcwd()}')
var_path = r'c:\Users\nerio\Desktop\Python\Proyectos\JPNtoPNGconverter'
# pathlib.P
os.chdir(var_path)

print(f'path final: {os.getcwd()}')
files = [f for f in os.listdir('.') if os.path.isfile(f)]

if not os.path.exists(var_path+dir1):
    os.mkdir(var_path+dir1)

if not os.path.exists(var_path+dir2):
    os.mkdir(var_path + dir2)
    print(f'Crea directorio: {var_path} + {dir2}')

for f in os.listdir(var_path+dir1):
    print(var_path+dir1+'\\'+f)
    print(var_path+dir2+'\\'+f)
#shutil.copy(var_path+dir1+'\\'+f, var_path+dir2+'\\'+f)
#img = Image.open(f)

# print(f)
#img.save(var_path+dir2+f+'.png', '.png')
# print(f)
