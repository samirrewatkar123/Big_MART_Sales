import sys

def error_message_details(error,error_details:sys):
    _,_,exc_tb=error_details.exc_info()
    file_name=exc_tb.tb_frame.f_code.co_filename
    error_msg='An error has bbeen occured in python script {file_name}  line number {exc_tb.tb_lineno} and error message is {error}'
    
    return error_msg


class MyException(Exception):
    def __init__(self,error_msg,error_details:sys):
        super.__init__(error_msg)
        self.error_msg=error_message_details(error_msg,error_details=error_details)
        
    def __str__(self):
        return self.error_msg