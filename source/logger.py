import os
from datetime import datetime
import logging

LOF_FILE  = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log" # file saved using this name
log_path = os.path.join(os.getcwd(),"logs",LOF_FILE)
os.makedirs(log_path, exist_ok=True)  # keep on appending files in logs folder

Log_FILE_PATH = os.path.join(log_path,LOF_FILE) # file with respect to file name

# creating logging to save info in the File
logging.basicConfig(

    filename=Log_FILE_PATH,
    format= "[%(asctime)s] %(lineno)d %(name)s %(levelname)s %(message)s",  # formate for storing msg in log_file
    level=logging.INFO  # in the case of INFO onlly i am going to print the msg
)

'''for checking the logger.py
if __name__ == "__main__":
    logging.info("Logging has strated")
'''


