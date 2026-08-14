import time
import random
import requests

def retry_request(url, max_retries=5, backoff_factor=0.3):
    retries = 0
    while retries < max_retries:
        try:
            response = requests.get(url)
            response.raise_for_status()  # Raises an HTTPError for bad responses
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Attempt {retries + 1} failed: {e}")
            retries += 1
            sleep_time = backoff_factor * (2 ** (retries - 1)) + random.uniform(0, 0.1)
            print(f"Retrying in {sleep_time:.2f} seconds...")
            time.sleep(sleep_time)
    raise Exception(f"Max retries exceeded for {url}")

# Example usage:
# data = retry_request('https://api.example.com/data')
