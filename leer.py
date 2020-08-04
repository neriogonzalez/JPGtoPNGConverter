import os
import shutil
from PIL import Image

dir1 = '\\Pokedex'
dir2 = '\\Nuevo'
var_path = (os.getcwd() + '\images\JPGtoPNGConverter')
os.chdir(var_path)
# files = [f for f in os.listdir('.') if os.path.isfile(f)]

if not os.path.exists(var_path+dir1):
    os.mkdir(var_path+dir1)

if not os.path.exists(var_path+dir2):
    os.mkdir(var_path+dir2)

for f in os.listdir(var_path+dir1):
    print(var_path+dir1+'\\'+f)
    print(var_path+dir2+'\\'+f)
    shutil.copy(var_path+dir1+'\\'+f, var_path+dir2+'\\'+f)
#img = Image.open(f)

# print(f)
#img.save(var_path+dir2+f+'.png', '.png')
# print(f)
