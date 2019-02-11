
import kNN
import unittest
import matplotlib
import matplotlib.pyplot as plt
from numpy import *

group, labels = kNN.createDataSet()

print(group)
print(labels)

result = kNN.classify0([0,0], group, labels, 3)

print(result)

datingDataMat, datingLabels = kNN.file2matrix('./data_analyse/maching_learning/kNN/datingTestSet.txt')

print(datingDataMat)

print(datingLabels)

fig = plt.figure()

ax = fig.add_subplot(111)

ax.scatter(datingDataMat[:,0], datingDataMat[:,1],
           15.0*array(datingLabels), 15.0*array(datingLabels))

plt.show()

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