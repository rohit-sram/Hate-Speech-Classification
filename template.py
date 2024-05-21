import os 
import sys 
from pathlib import Path 
import logging

logging.basicConfig(level=logging.INFO, format="[%(asctime)s]: %(message)s: ")

list_of_files = [
    f"components/__init__.py",
    f"components/data_ingestion.py",
    f"components/data_transformation.py",
    f"components/model_trainer.py",
    f"components/model_evaluation.py",
    f"components/model_pusher.py",
    f"configuration/__init__.py",
    f"configuration/gcloud_sync.py",
    f"constants/__init__.py",
    f"entity/__init__.py",
    f"entity/config_entity.py",
    f"entity/artifact_entity.py",
    f"exception/__init__.py",
    f"logger/__init__.py",
    f"pipeline/__init__.py",
    f"pipeline/training_pipeline.py",
    f"pipeline/prediction_pipeline.py",
    f"ml/__init__.py",
    f"ml/model.py",
    "app.py",
    "demo.py",
    "requirements.txt",
    "Dockerfile", 
    "setup.py", 
    ".dockerignore"
]

for file_path in list_of_files:
    file_path = Path(file_path)
    
    file_dir, file_name = os.path.split(file_path)
    
    if (file_dir != ""):
        os.makedirs(file_dir, exist_ok=True)
        logging.info(f"Creating folder {file_dir} for file: {file_name}")
        
    if (not os.path.exists(file_path)) or (os.path.getsize(file_path) == 0):
        with open(file_path, "w") as fobj:
            logging.info(f"Creating empty file: {file_path}")
            pass
        
    else: 
        logging.info(f"{file_name} already exists")