import time

class GameProcessor:
    def __init__(self, initial_data):
        self.data = initial_data
        self.results = []

    def process_data(self):
        start = time.perf_counter()
        self.results = [self.expensive_operation(d) for d in self.data]
        end = time.perf_counter()
        print(f'Processing time: {end - start:.4f} seconds')

    def expensive_operation(self, d):
        return d ** 2  # Simulating heavy computation

    def get_results(self):
        return self.results

# Sample usage
if __name__ == '__main__':
    processor = GameProcessor(range(10000))
    processor.process_data()
    print(processor.get_results()[:10])  # Print first 10 results