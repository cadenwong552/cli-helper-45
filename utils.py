import time
import random
import requests

def retry_on_failure(max_retries=3, wait_time=2, backoff=2):
    def decorator(func):
        def wrapper(*args, **kwargs):
            retries = 0
            while retries < max_retries:
                try:
                    return func(*args, **kwargs)
                except (requests.ConnectionError, requests.Timeout) as e:
                    print(f"Attempt {retries + 1} failed: {e}")
                    time.sleep(wait_time)
                    wait_time *= backoff
                    retries += 1
            print("All attempts failed.")
            return None
        return wrapper
    return decorator

@retry_on_failure(max_retries=5, wait_time=1)
def fetch_data(url):
    response = requests.get(url)
    response.raise_for_status()
    return response.json()

if __name__ == '__main__':
    data = fetch_data('https://api.example.com/data')
    print(data)