import sys
import time

#before
# class Logger:
#
#     def log(self, message):
#         current_time = time.localtime()
#         sys.stderr.write(f'{time.strftime("%Y-%b-%d %H:%M:%S", current_time)} --> {message}')
#
#
# logger = Logger()
# logger.log('Something wrong')


#after


class Logger:

    def __init__(self):
        self.format = "%Y-%b-%d %H:%M:%S"

    def log(self, message):
        current_time = time.localtime()
        sys.stderr.write(f'{time.strftime(self.format, current_time)} --> {message}')


class CustomerLogger(Logger):

    def __init__(self):
        super().__init__()
        self.format = "%Y-%b-%d"


logger = Logger()
logger.log('Something wrong\n')


customer_logger = CustomerLogger()
customer_logger.log('Customer logger')