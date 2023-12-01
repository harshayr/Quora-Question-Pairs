import sys # store the error details
from source.logger import logging
# sys.path.insert(0, '../source')
# import unittest
# from logger import logging

def error_msg_details(error, error_detail:sys):  # getting details of error msg
   
#    error_detail.exc_info() this will return three values but we want only one so

   _,_,exc_tb = error_detail.exc_info()
   file_name = exc_tb.tb_frame.f_code.co_filename  # here we get the filename
   error_msg = "Error occured in python scrip name [{0}] line number [{1}] error messege [{2}]".format(file_name, exc_tb.tb_lineno,str(error)  )                                                                                               
   return error_msg                                                                                                
   
class CustomException(Exception):
   def __init__(self, error_msg, error_details:sys):
      super().__init__(error_msg)   # getting error_msg from parent class i.e Exception
      self.error_msg = error_msg_details(error_msg,error_detail= error_details)

   def __str__(self):
       return self.error_msg



''' just to check exception working or not
if __name__ == "__main__":
   try:
      a = 1/0
   except Exception as e:
      logging.info("Acannot diveded by zero")
      raise CustomException(e,sys)
'''



