import time

import requests
from loguru import logger


URL = 'http://localhost:5000/'


while True:
    time.sleep(5)
    response = requests.get(URL)
    if response.status_code == 200:
        logger.debug('All ok, server is run')
        print('All good')
    else:
        print('Something wrong !!! ')
