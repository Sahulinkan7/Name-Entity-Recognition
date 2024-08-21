import sys

class NerException(Exception):
    def __init__(self,error_message:Exception,error_details:sys):
        super().__init__(error_message)
        self.error_message=NerException.get_error_message_details(error_message,error_details)
        
    def __str__(self) -> str:
        return self.error_message
            
    @staticmethod
    def get_error_message_details(error_message:Exception,error_details:sys):
        """
        Args:
            error_message (Exception): _description_
            error_details (sys): _description_
        """
        _, _,exc_trace=error_details.exc_info()
        
        filename=exc_trace.tb_frame.f_code.co_filename
        line_number=exc_trace.tb_lineno
        
        error_message=f"""
        Exception occured in script file {filename}, line numer {line_number},
        error message is {str(error_message)}
        """
        
        return error_message