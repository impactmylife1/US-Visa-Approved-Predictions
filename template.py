import os # we need the operating system
from pathlib import Path

project_name = "US-Visa"  # root folder

list_of_files = [
    # __init__.py means construct to file
    f"{project_name}/__init__.py", # this is for the root folder of the project
    f"{project_name}/components/__init__.py", # this is for the sub folder 
    f"{project_name}/components/data_ingestion.py", # this is the file under components
    f"{project_name}/components/data_validation.py", # fil
    f"{project_name}/components/data_transformation.py", # file
    f"{project_name}/components/model_trainer.py", # file
    f"{project_name}/components/model_evaluation.py", # file
    f"{project_name}/components/model_pusher.py", # file
    f"{project_name}/configuration/__init__.py",
    f"{project_name}/constants/__init__.py",
    f"{project_name}/entity/__init__.py",
    f"{project_name}/entity/artifact_entity.py",
    f"{project_name}/entity/config_entity.py",
    f"{project_name}/exception/__init__.py",
    f"{project_name}/logger/__init__.py",
    f"{project_name}/pipeline/__init__.py",
    f"{project_name}/pipeline/training_pipeline.py",
    f"{project_name}/pipeline/prediction_pipeline.py",
    f"{project_name}/utils/main_utils.py",
    "app.py",
    "requirements.txt",
    "Dockerfile",
    ".dockerignore",
    "demo.py",
    "setup.py",
    "config/model.yaml",
    "config/schema.yaml"
    "test.py"

]

for filepath in list_of_files:
    filepath = Path(filepath) # converting the path to the present web browswer or operating system
    filedir, filename = os.path.split(filepath) #seperating the path into file directory (folder) and filename(file)
    if filedir != "": # if the file directory is not empty
        os.makedirs(filedir, exist_ok=True) # create a directory
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
    else:
        print(f"file is already present at: {filepath}")