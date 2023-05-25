import logging

import requests

logging.basicConfig(level=logging.INFO, filename='my_log.log', filemode='w',
                    format="%(asctime)s %(levelname)s %(message)s")

# logging.debug('Debug')
# logging.info('Info')
# logging.warning('Warning')
# logging.error('Error')
# logging.critical('Critical')

# debit = 100
# credit = 50
# if credit < debit:
#     logging.warning(f'It"s impossible credit {credit} should be < {debit}', exc_info=True)

# x = 3
# y = 5
#
# logging.info(f"We get value {x} and {y}")
# try:
#     result = x/y
#     logging.info(f"x/y successful with result {result}")
# except ZeroDivisionError as err:
#     logging.warning("ZeroDivisionError", exc_info=True)


x_value = [1, 2, 3, 0, 43, 1]
y_value = [11, 0, 13, 23, 234, 0, 23]


for x_value, y_value in zip(x_value, y_value):
    x, y = x_value, y_value
    try:
        result = x / y
        logging.info(f"x/y successful with result {result}")
    except ZeroDivisionError as err:
        logging.warning("ZeroDivisionError", exc_info=True)




