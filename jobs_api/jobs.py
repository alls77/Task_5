# используя API Получить информацию с 2х страниц о 3х разных JOB
# https://jobs.github.com/positions.json?description={description_name}&page={page}

import requests
from threading import Thread

from utils import logger, timer

URL = 'https://jobs.github.com/positions.json'
PAGE_COUNT = 2


def get_response(parameters: dict, url):
    return requests.get(url, params=parameters).content


@logger
def get_jobs(parameters: dict, pages=PAGE_COUNT, url=URL):
    result = []
    for item in range(1, pages + 1):
        parameters['page'] = item
        result.append(get_response(parameters, url))
    return result


def create_threads(target, args):
    threads = []
    for arg in args:
        threads.append(Thread(target=target, args=(arg,)))
    return threads


def start_threads(threads):
    for thread in threads:
        thread.start()


def join_threads(threads):
    for thread in threads:
        thread.join()


@timer
def main():
    data = [
        {
            'description': 'c#',
        },
        {
            'description': 'java',
            'location': 'USA',
        },
        {
            'description': 'python',
            'full_time': 'true',
        },
    ]
    threads = create_threads(get_jobs, data)
    start_threads(threads)
    join_threads(threads)


if __name__ == '__main__':
    main()
