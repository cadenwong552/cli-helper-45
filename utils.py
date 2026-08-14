import time
import random
import requests

class NetworkError(Exception):
    pass

def retry_with_exponential_backoff(func, max_attempts=5, base_delay=1, max_delay=60):
    attempts = 0
    while attempts < max_attempts:
        try:
            return func()
        except NetworkError:
            attempts += 1
            delay = min(base_delay * (2 ** (attempts - 1)), max_delay)
            print(f'Retrying in {delay} seconds...')
            time.sleep(delay)
    raise NetworkError('Max attempts reached')

def fetch_data(url):
    response = requests.get(url)
    if response.status_code != 200:
        raise NetworkError(f'Error fetching data: {response.status_code}')
    return response.json()

# Example usage:
# result = retry_with_exponential_backoff(lambda: fetch_data('https://api.example.com/data'))
