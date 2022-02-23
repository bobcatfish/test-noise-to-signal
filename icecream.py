import collections
import random


class NetworkException(Exception):
    pass


class Orders:
    def __init__(self):
        self.orders = collections.defaultdict(list)

    def add(self, date, order):
        self.orders[date].append(order)

    def get_most_recent(self):
        most_recent_key = list(self.orders)[-1]
        return self.orders[most_recent_key][0]


class MrFreezie():
    def connect(self):
        if not bool(random.getrandbits(1)):
            raise NetworkException("NETWORK TROUBLE")
        pass

    def process_order(self, order):
        return []
