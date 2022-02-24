import collections
import random


class NetworkException(Exception):
    pass


class Orders:
    def __init__(self):
        self.totalOrders = 0
        self.orders = collections.defaultdict(list)

    def add(self, date, order):
        self.totalOrders += 1
        self.orders[date].append(order)

    def get_most_recent(self):
        most_recent_key = sorted(self.orders.keys())[-1]
        return self.orders[most_recent_key][0]

    def get_total_orders(self):
        return self.totalOrders

    def submit_orders(self, service):
        for _, order in self.orders.items():
            service.process_order(order)
        self.orders.clear()


class MrFreezie():
    def connect(self):
        if not bool(random.getrandbits(1)):
            raise NetworkException("NETWORK TROUBLE")
        pass

    def process_order(self, order):
        # pretend some cool order processing is happening here
        return []