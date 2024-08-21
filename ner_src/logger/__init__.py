import logging 
import os,sys 
from ner_src.constants import * 

log_path=os.path.join(os.getcwd(),"logs",TIMESTAMP)

os.makedirs(log_path,exist_ok=True)

log_file_path=os.path.join(log_path,LOGS_FILE_NAME)

logging.basicConfig(
    filename=log_file_path,
    level=logging.INFO,
    format="[%(asctime)s] %(name)s %(levelname)s %(lineno)s %(message)s"
)

