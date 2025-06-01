"""
рекурсивно копіює файли у вихідній директорії, 
переміщає їх до нової директорії та 
сортує в піддиректорії, 
назви яких базуються на розширенні файлів.

NOTES
elementS - element(file/folder) from source
elementD - element(file/folder) from distination
"""
import sys
from pathlib import Path
import shutil


listArgs = sys.argv
listArgs = ["0","/Users/mariashukaliuk/Desktop/Algorithms/test_source",
            "/Users/mariashukaliuk/Desktop/Algorithms/test_distination"]
pathSource = listArgs[1]
pathDist = listArgs[2]

source = Path(pathSource)
distination = Path(pathDist)

def read_dir(pathToSource):
    try:
        for elementS in pathToSource.iterdir():
            if elementS.is_dir():
                read_dir(elementS)
            else:
                copy_func(elementS, distination)
    except:  
        print("Something went wrong") 

def copy_func(elementS, fileDistination):
    subFolder = str(elementS).split('.')[-1]
    for elementD in fileDistination.iterdir():
        if str(elementD).split('/')[-1] == subFolder:
            subFolderPathVar = Path((str(fileDistination) + "/" + subFolder))
            shutil.copy(elementS, subFolderPathVar)
    else:
        target_folder = fileDistination / subFolder
        target_folder.mkdir(parents=True, exist_ok=True)
        shutil.copy(elementS, target_folder)

read_dir(source)

"""

cd /Users/mariashukaliuk/Desktop/Algorithms/
python3 HW_3.Shukaliuk.py test_source test_distination

/Users/mariashukaliuk/Desktop/Algorithms/test_source
/Users/mariashukaliuk/Desktop/Algorithms/test_distination


Завдання 2

Напишіть програму на Python, 
використовує рекурсію для створення фракталу 
«сніжинка Коха» 
користувач повинен мати можливість вказати рівень рекурсії.

"""

import turtle

user_input = int(input('Enter fractal lvl: '))
order = user_input

def koch_curve(t, order, size):
    if order == 0:
        t.forward(size)
    else:
        koch_curve(t, order - 1, size / 3)
        t.left(60)
        koch_curve(t, order - 1, size / 3)
        t.right(120)
        koch_curve(t, order - 1, size / 3)
        t.left(60)
        koch_curve(t, order - 1, size / 3)

def draw_koch_curve(order, size=300):
    window = turtle.Screen()
    window.bgcolor("white")

    t = turtle.Turtle()
    t.speed(0)  
    t.penup()
    t.goto(-size / 2, 0)
    t.pendown()

    koch_curve(t, order, size)

    t.hideturtle()
    window.mainloop()

draw_koch_curve(order) 
