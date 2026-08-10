import time
from functools import lru_cache

@lru_cache(maxsize=128)
def expensive_computation(x):
    time.sleep(2)  # Simulate a time-consuming computation
    return x * x

def process_numbers(numbers):
    results = []
    for number in numbers:
        result = expensive_computation(number)
        results.append(result)
    return results

if __name__ == '__main__':
    numbers = list(range(5))
    print(process_numbers(numbers))
    print(process_numbers(numbers))  # This will be faster due to caching