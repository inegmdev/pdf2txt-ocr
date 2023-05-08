import inspect

class Logger:
    def __init__(self, class_name: str):
        self.class_name = class_name
    
    def info(self, msg: str):
        # [1] to get the frame record for the caller function (i.e., the second item in the list)
        # and [3] to get the name of the function from the frame record.
        caller_func_name = inspect.stack()[1][3]
        print(f'[INFO] ({self.class_name}->{caller_func_name}): {msg}')
