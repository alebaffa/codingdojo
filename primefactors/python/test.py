import unittest

from prime_factors import compute

# @TODO: maybe force the order of the output of compute

class TestSuite(unittest.TestCase):

    def helper_test(self, number, expected):
        actual = compute(number)
        self.assertEquals(
            expected,
            actual,
            "Prime factor(s) for %s returned %s but should be %s." % (
                number, actual, expected))

    def test_exists(self):
        compute(0)

    def test_returns_list(self):
        result = compute(0)
        self.assertTrue(
            isinstance(result, list), "Generate should return a list")

    def test_no_prime_factor_for_zero(self):
        result = compute(0)
        self.assertEquals([], result, "Zero has no prime factors")

    def test_1(self):
        self.assertEquals([], compute(1), "There is no prime factor for 1.")

    def test_2(self):
        self.helper_test(2, [2])

    def test_3(self):
        self.helper_test(3, [3])

    def test_4(self):
        self.helper_test(4, [2, 2])

    def test_6(self):
        self.helper_test(6, [2, 3])

    def test_8(self):
        self.helper_test(8, [2, 2, 2])

    def test_25(self):
        self.helper_test(25, [5, 5])

    def test_7(self):
        self.helper_test(7, [7])

    def test_powers_of_two(self):
        number = 1
        expected = []
        for i in range(1, 10):
            number *= 2
            expected.append(2)
            self.helper_test(number, expected)

if __name__ == '__main__':
   unittest.main()
