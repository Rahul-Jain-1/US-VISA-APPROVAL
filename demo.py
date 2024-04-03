from us_visa.logger import logging
from us_visa.exception import USvisaException
# /config/workspace/us_visa/exception
import sys
# custom log
# logging.info("This is the custom log file")

# how it will show the error 
try:
    a = 1 / 1
except Exception as e:
    logging.info(e)
    raise USvisaException(e,sys) from e'
