import unittest

import numpy as np

from config import *
from utils import *


class TestStringMethods(unittest.TestCase):

    def test_KNN(self):
        test_attr_1 = parse_attributes(
            '[ 1.00 0.00 0.00 0.00 1.00 0.00 0.00 0.00 0.00 0.00 1.00 0.00 1.00 0.00 1.00 0.00 0.00 0.00 0.00 1.00 0.00 0.00 1.00 0.00 0.00 1.00 0.00 0.00 1.00 0.00 1.00 0.00 1.00 0.00 0.00 0.00 0.00 0.00 1.00 1.00 0.00 0.00 1.00 1.00 1.00 0.00 0.00 1.00 1.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 1.00 1.00 0.00 1.00 1.00 0.00 1.00 1.00 0.00 1.00 0.00 1.00 0.00 0.00 0.00 0.00 0.00 0.00 1.00 0.00 0.00 0.00 1.00 0.00 1.00 0.00 1.00 1.00 0.00 0.00 1.00 1.00 0.00 0.00 1.00 0.00 0.00 1.00 0.00 0.00 1.00 1.00 0.00 0.00 1.00 0.00 0.00 0.00 0.00 0.00 1.00 0.00 1.00 1.00 0.00 1.00 0.00 0.00 0.00 0.00 1.00 0.00 ]')
        test_attr_1 = torch.tensor(test_attr_1)
        # print(test_attr.size())
        val, index = KNN(test_attr_1 - attributes_per_class, 1)
        self.assertEqual(index.item(), 5)

        test_attr_2 = parse_attributes(
            '[ 0.00 0.00 0.00 0.00 0.00 1.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 1.00 0.00 1.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 1.00 0.00 1.00 0.00 1.00 0.00 0.00 0.00 0.00 0.00 0.00 1.00 0.00 0.00 1.00 1.00 0.00 0.00 0.00 1.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 1.00 1.00 0.00 1.00 1.00 0.00 1.00 1.00 0.00 1.00 0.00 0.00 0.00 0.00 1.00 0.00 0.00 1.00 0.00 1.00 0.00 0.00 1.00 0.00 1.00 0.00 1.00 1.00 1.00 0.00 1.00 1.00 0.00 0.00 0.00 0.00 1.00 0.00 0.00 0.00 1.00 1.00 0.00 0.00 1.00 0.00 0.00 0.00 0.00 1.00 0.00 0.00 0.00 0.00 0.00 1.00 0.00 0.00 0.00 0.00 1.00 1.00 ]')
        test_attr_2 = torch.tensor(test_attr_2)
        val, index = KNN(test_attr_2 - attributes_per_class, 1)
        self.assertEqual(index.item(), 10)

        test_attr_3 = parse_attributes(
            '[ 0.00 1.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 1.00 0.00 0.00 1.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 1.00 0.00 0.00 1.00 0.00 1.00 0.00 1.00 1.00 0.00 0.00 1.00 1.00 0.00 0.00 1.00 0.00 0.00 0.00 0.00 1.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 1.00 0.00 0.00 1.00 1.00 0.00 1.00 1.00 0.00 1.00 1.00 1.00 1.00 1.00 0.00 0.00 1.00 1.00 1.00 1.00 1.00 0.00 1.00 0.00 0.00 1.00 0.00 0.00 1.00 1.00 0.00 1.00 1.00 0.00 1.00 0.00 0.00 0.00 0.00 1.00 0.00 0.00 1.00 0.00 1.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 1.00 0.00 0.00 0.00 0.00 0.00 ]')
        test_attr_3 = torch.tensor(test_attr_3)
        val, index = KNN(test_attr_3 - attributes_per_class, 1)
        self.assertEqual(index.item(), 27)

        test_attr_4 = parse_attributes(
            '[ 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 1.00 0.00 1.00 1.00 0.00 0.00 0.00 0.00 1.00 0.00 0.00 0.00 0.00 0.00 0.00 1.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 1.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 1.00 0.00 1.00 0.00 1.00 0.00 0.00 0.00 1.00 0.00 0.00 0.00 0.00 0.00 0.00 1.00 0.00 0.00 0.00 1.00 0.00 1.00 1.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 1.00 0.00 1.00 0.00 0.00 0.00 0.00 0.00 ]')
        test_attr_4 = torch.tensor(test_attr_4)
        val, index = KNN(test_attr_4 - attributes_per_class, 1)
        self.assertEqual(index.item(), 36)

        test_attr_5 = parse_attributes(
            '[ 0.00 0.00 0.00 0.00 1.00 1.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 1.00 1.00 0.00 0.00 0.00 1.00 1.00 0.00 1.00 0.00 0.00 0.00 0.00 1.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 1.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 1.00 1.00 0.00 1.00 0.00 1.00 1.00 0.00 0.00 0.00 0.00 0.00 0.00 1.00 0.00 1.00 0.00 1.00 0.00 0.00 1.00 1.00 0.00 0.00 1.00 0.00 0.00 1.00 1.00 0.00 1.00 0.00 0.00 0.00 0.00 1.00 0.00 0.00 0.00 1.00 0.00 1.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 1.00 0.00 0.00 0.00 0.00 0.00 ]')
        test_attr_5 = torch.tensor(test_attr_5)
        val, index = KNN(test_attr_5 - attributes_per_class, 1)
        self.assertEqual(index.item(), 43)

    def test_batched_KNN(self):
        mat = [parse_attributes(
            '[ 1.00 0.00 0.00 0.00 1.00 0.00 0.00 0.00 0.00 0.00 1.00 0.00 1.00 0.00 1.00 0.00 0.00 0.00 0.00 1.00 0.00 0.00 1.00 0.00 0.00 1.00 0.00 0.00 1.00 0.00 1.00 0.00 1.00 0.00 0.00 0.00 0.00 0.00 1.00 1.00 0.00 0.00 1.00 1.00 1.00 0.00 0.00 1.00 1.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 1.00 1.00 0.00 1.00 1.00 0.00 1.00 1.00 0.00 1.00 0.00 1.00 0.00 0.00 0.00 0.00 0.00 0.00 1.00 0.00 0.00 0.00 1.00 0.00 1.00 0.00 1.00 1.00 0.00 0.00 1.00 1.00 0.00 0.00 1.00 0.00 0.00 1.00 0.00 0.00 1.00 1.00 0.00 0.00 1.00 0.00 0.00 0.00 0.00 0.00 1.00 0.00 1.00 1.00 0.00 1.00 0.00 0.00 0.00 0.00 1.00 0.00 ]'),
            parse_attributes(
                '[ 0.00 0.00 0.00 0.00 0.00 1.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 1.00 0.00 1.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 1.00 0.00 1.00 0.00 1.00 0.00 0.00 0.00 0.00 0.00 0.00 1.00 0.00 0.00 1.00 1.00 0.00 0.00 0.00 1.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 1.00 1.00 0.00 1.00 1.00 0.00 1.00 1.00 0.00 1.00 0.00 0.00 0.00 0.00 1.00 0.00 0.00 1.00 0.00 1.00 0.00 0.00 1.00 0.00 1.00 0.00 1.00 1.00 1.00 0.00 1.00 1.00 0.00 0.00 0.00 0.00 1.00 0.00 0.00 0.00 1.00 1.00 0.00 0.00 1.00 0.00 0.00 0.00 0.00 1.00 0.00 0.00 0.00 0.00 0.00 1.00 0.00 0.00 0.00 0.00 1.00 1.00 ]'),
            parse_attributes(
                '[ 0.00 1.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 1.00 0.00 0.00 1.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 1.00 0.00 0.00 1.00 0.00 1.00 0.00 1.00 1.00 0.00 0.00 1.00 1.00 0.00 0.00 1.00 0.00 0.00 0.00 0.00 1.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 1.00 0.00 0.00 1.00 1.00 0.00 1.00 1.00 0.00 1.00 1.00 1.00 1.00 1.00 0.00 0.00 1.00 1.00 1.00 1.00 1.00 0.00 1.00 0.00 0.00 1.00 0.00 0.00 1.00 1.00 0.00 1.00 1.00 0.00 1.00 0.00 0.00 0.00 0.00 1.00 0.00 0.00 1.00 0.00 1.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 1.00 0.00 0.00 0.00 0.00 0.00 ]'),
            parse_attributes(
                '[ 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 1.00 0.00 1.00 1.00 0.00 0.00 0.00 0.00 1.00 0.00 0.00 0.00 0.00 0.00 0.00 1.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 1.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 1.00 0.00 1.00 0.00 1.00 0.00 0.00 0.00 1.00 0.00 0.00 0.00 0.00 0.00 0.00 1.00 0.00 0.00 0.00 1.00 0.00 1.00 1.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 1.00 0.00 1.00 0.00 0.00 0.00 0.00 0.00 ]'),
            parse_attributes(
                '[ 0.00 0.00 0.00 0.00 1.00 1.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 1.00 1.00 0.00 0.00 0.00 1.00 1.00 0.00 1.00 0.00 0.00 0.00 0.00 1.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 1.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 1.00 1.00 0.00 1.00 0.00 1.00 1.00 0.00 0.00 0.00 0.00 0.00 0.00 1.00 0.00 1.00 0.00 1.00 0.00 0.00 1.00 1.00 0.00 0.00 1.00 0.00 0.00 1.00 1.00 0.00 1.00 0.00 0.00 0.00 0.00 1.00 0.00 0.00 0.00 1.00 0.00 1.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 1.00 0.00 0.00 0.00 0.00 0.00 ]')
        ]
        mat = torch.tensor(mat)
        val_list, index_list = batched_KNN(mat, 1)
        print(index_list)
        self.assertTrue(np.array_equal(index_list.cpu().numpy(), np.array([5, 10, 27, 36, 43])))

    def test_accuracy(self):
        targets = torch.tensor([12, 35, 15, 3, 37, 18, 42, 46, 16, 39, 37, 47, 48, 44, 16, 10], device=device)
        scores = torch.tensor([34, 34, 34, 34, 34, 34, 34, 34, 34, 34, 34, 34, 34, 34, 34, 34], device=device)
        acc = accuracy(scores, targets)
        print('acc: ' + str(acc))


if __name__ == '__main__':
    unittest.main()
