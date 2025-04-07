import random
import time

def generate_simulated_data():
    """Rastgele manyetik veri üretir"""
    while True:
        value = random.randint(100, 220)  # 100-220 arası değerler
        yield value
        time.sleep(0.5)  # 0.5 saniyede bir veri gelsin
