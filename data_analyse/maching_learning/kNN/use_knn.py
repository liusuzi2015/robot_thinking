
import kNN
import unittest

group, labels = kNN.createDataSet()

print(group)
print(labels)

result = kNN.classify0([0,0], group, labels, 3)

print(result)

class TestkNN(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_kNN(self):
        group, labels = kNN.createDataSet()
        result = kNN.classify0([0, 0], group, labels, 3)
        expected = 'B'
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()