import unittest 
from unittest import TestCase
from price_discount import discount  

class TestDiscount(TestCase):

    def test_list_of_three_prices(self):
        prices = [10, 4, 20]
        expected_discount = 4
        self.assertEqual(expected_discount, discount(prices))

    
    # TODO more unit tests here. Each test should test one scenario

    def test_list_of_two_prices_no_discount(self):
        prices = [10, 4]
        expected_discount = 0
        calculated_discount = discount(prices)
        self.assertEqual(expected_discount, calculated_discount)

    def test_list_of_one_price_no_discount(self):
        self.fail()

    def test_list_of_more_than_three_prices(self):
        self.fail()

    def test_list_no_items_no_discount(self):
        self.fail()

    def test_list_negative_value_raises_exception(self):
        self.fail()

    def test_list_two_items_same_price(self):
        self.fail()

    def test_list_more_than_two_items_same_price(self):
        self.fail()

    def test_list_with_floats(self):
        self.fail()

    def test_list_with_currency_unit_raises_exception(self):
        self.fail()

    def test_list_with_strings_no_int_raises_exception(self):
        self.fail()

    def test_list_with_zero_value_items(self):
        self.fail()



if __name__ == '__main__':
    unittest.main()