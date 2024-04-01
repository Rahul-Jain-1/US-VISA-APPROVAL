#  logger file will track of all bug happenend in the development time and save them inside logs folder
# let suppose morining time we got 1 bug 
# and in evening time we again got 1 bug  
# then using log file we can check what was morning bug

import logging
import os
from from_root import from_root
from datetime import datetime
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log "
log_dir = "logs"
logs_path = os.path.join(from_root(),log_dir,LOG_FILE)
os.makedirs(log_dir,exist_ok=True)

logging.basicConfig(
    filename=logs_path,
    format="[%(asctime)s] %(name)s - %(levelname)s - %(message)s",
    level=logging.DEBUG
)