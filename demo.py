from us_visa.logger import logging
from us_visa.exception import USvisaException
import sys
# custom log
# logging.info("This is the custom log file")

# how it will show the error 
try:
    a = 1 / "10"
except Exception as e:
    raise USvisaException(e,sys) from e
