#Python script for project
import os ,sys 
from pathlib import Path 
import logging

while True:
    project_name = input("Enter your project nam:-")
    
    if project_name !="":
        break



list_of_file = [
    f"src/{project_name}/__init__.py" ,
    # f"src/{project_name}/components/__init__.py",
    # f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/logger/__init__.py",
    f"src/{project_name}/exception/__init__.py",
    f"src/{project_name}/pipeline/__init__.py",
    # f"src/{project_name}/entity/__init__.py" ,
    f"src/__init__.py" ,
    f"src/{project_name}/utils/__init__.py" ,
    f"templates/index.html" ,
    f"app.py"
]

for filepath in list_of_file:
    filepath =Path(filepath) 
    filedir ,filename =os.path.split(filepath)
    
    if filedir != "":
        os.makedirs(filedir ,exist_ok=True)
        
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath , 'w') as f:
            pass
    else:
        logging.info('file is already present at : {filepath}')
        
        