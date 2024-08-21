import os
from pathlib import Path 
import logging

logging.basicConfig(level=logging.INFO,format='[%(asctime)s: %(message)s]')


project_name = "ner_src"

list_of_files=[
    f"{project_name}/__init__.py",
    f"{project_name}/entity/__init__.py",
    f"{project_name}/entity/config_entity.py",
    f"{project_name}/entity/artifact_entity.py",
    f"{project_name}/components/__init__.py",
    f"{project_name}/components/data_ingestion.py",
    f"{project_name}/components/data_transformation.py",
    f"{project_name}/components/model_trainer.py",
    f"{project_name}/components/model_evaluation.py",
    f"{project_name}/components/model_pusher.py",
    f"{project_name}/configuration/__init__.py",
    f"{project_name}/configuration/gcloud.py",
    f"{project_name}/constants/__init__.py",
    f"{project_name}/logger/__init__.py",
    f"{project_name}/exception/__init__.py",
    f"{project_name}/pipeline/__init__.py",
    f"{project_name}/pipeline/tain_pipeline.py",
    f"{project_name}/pipeline/prediction_pipeline.py",
    "app.py",
    "train.py",
    "requirements.txt",
    "Dockerfile",
    ".dockerignore",
    "setup.py"
]


for filepath in list_of_files:
    filepath=Path(filepath)
    
    dir,filename=os.path.split(filepath)
    if dir!="":
        os.makedirs(dir,exist_ok=True)
        logging.info(f"creating file directory {dir} for file {filename}")
    
    if not (os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        with open(filepath,"w") as file:
            pass
            logging.info(f"file created successfully !")
    else:
        logging.info(f"file already exist !")