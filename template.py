 import os
import logging
from pathlib import Path

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

Project_name = "textsummarizer"

list_of_files = [
    ".github/workflows/.gitkeep",

    f"src/{Project_name}/_init_.py",
    f"src/{Project_name}/components/_init_.py",
    f"src/{Project_name}/utils/_init_.py",
    f"src/{Project_name}/utils/common.py",
    f"src/{Project_name}/logging/_init_.py",
    f"src/{Project_name}/config/_init_.py",
    f"src/{Project_name}/config/configuration.py",
    f"src/{Project_name}/pipeline/_init_.py",
    f"src/{Project_name}/entity/_init_.py",
    f"src/{Project_name}/constants/_init_.py",

    "config/config.yaml",
    "params.yaml",
    "app.py",
    "main.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
    
]

for filepath in list_of_files:
    filepath = Path(filepath)

    filedir = filepath.parent

    if filedir != Path("."):
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir}")

    if not filepath.exists():
        with open(filepath, "w") as f:
            pass
        logging.info(f"Creating empty file: {filepath}")

    else:
        logging.info(f"{filepath.name} already exists")