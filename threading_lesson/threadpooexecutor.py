import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from time import perf_counter

import requests


def get_wiki(url):

    response = requests.get(url=url)
    status = 'unknown'

    if response.status_code == 200:
        status = 'exist'
    elif response.status_code == 404:
        status = 'does not exist'
    return url + status

wiki_page_urls = ["https://en.wikipedia.org/wiki/" + str(i) for i in range(50)]

start_time = perf_counter()

with ThreadPoolExecutor() as executor:
    # futures = []
    # for url in wiki_page_urls:
    #     futures.append(executor.submit(get_wiki, url))
    futures = [executor.submit(get_wiki, url) for url in wiki_page_urls]
    for future in as_completed(futures):
        print(future.result())

end_time = perf_counter()
print(f'Time to execute {end_time- start_time: 0.2f} second.')



