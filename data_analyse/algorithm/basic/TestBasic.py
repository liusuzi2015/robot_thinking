
import unittest
import basic

class TestGcd(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_kNN(self):
        result = basic.gcd(4,6)
        expected = 2
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()

