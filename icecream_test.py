import collections
import datetime
import unittest

import icecream


class IceCreamProviderFake():
    def connect(self):
        # no flakey connection here
        pass

    def process_order(self, order):
        # pretend some cool order processing is happening here
        return []


def _get_seeded_orders():
    orders = icecream.Orders()
    orders.add(datetime.date(2020, 9, 4), "swirl cone")
    orders.add(datetime.date(2020, 9, 10), "rainbow sprinkle")
    orders.add(datetime.date(2020, 9, 7), "cherry glazed")
    return orders


class TestOrder(unittest.TestCase):

    def test_add_item_multiple(self):
        '''This test passes and should'''
        orders = _get_seeded_orders()

        expectedOrders = collections.defaultdict(list, {
            datetime.date(2020, 9, 7): ["cherry glazed"],
            datetime.date(2020, 9, 4): ["swirl cone"],
            datetime.date(2020, 9, 10): ["rainbow sprinkle"],
        })

        self.assertDictEqual(orders.orders, expectedOrders)

    def test_get_most_recent(self):
        '''This test passes, but shouldn't'''
        orders = _get_seeded_orders()
        most_recent = orders.get_most_recent()
        self.assertEqual(most_recent, "rainbow sprinkle")

    @unittest.skip("This test will fail - on purpose!")
    def test_submit_orders(self):
        '''This test will fail because the logic is broken'''
        orders = _get_seeded_orders()

        provider = IceCreamProviderFake()
        provider.connect()

        orders.submit_orders(provider)
        self.assertEqual(len(orders.orders), 0)

    @unittest.skip("This test will fail - on purpose!")
    def test_get_total_orders(self):
        '''This test will fail b/c the test is broken'''
        orders = _get_seeded_orders()
        self.assertEqual(orders.get_total_orders(), 0)


def _generate_mr_freezie_order():
    '''Just a dummy method for demo purposes'''
    return []


def _assert_order_updated(o):
    '''Just a dummy method for demo purposes'''
    pass


class TestMrFreezie(unittest.TestCase):

    def test_process_order(self):
        ''' This is a flakey test! '''
        order = _generate_mr_freezie_order()
        mrf = icecream.MrFreezie()
        mrf.connect()
        mrf.process_order(order)
        _assert_order_updated(order)



if __name__ == '__main__':
    unittest.main()
