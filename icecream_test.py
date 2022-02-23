import datetime
import unittest

import icecream


class TestOrder(unittest.TestCase):

    def test_get_most_recent(self):
        '''This test passes, but shouldn't'''
        orders = icecream.Orders()
        orders.add(datetime.date(2020, 9, 4), "swirl cone")
        orders.add(datetime.date(2020, 9, 7), "cherry glazed")
        orders.add(datetime.date(2020, 9, 10), "rainbow sprinkle")

        most_recent = orders.get_most_recent()
        self.assertEqual(most_recent, "rainbow sprinkle")


if __name__ == '__main__':
    unittest.main()
