# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import unittest
import pandas as pd

import sys
sys.path.append("..")

from p2 import corruption_checksum

class TestCorruptionChecksum(unittest.TestCase):

    def test_corruption_checksum_m1(self):
        df = pd.read_csv("../p2_test_sheet.csv",header=None)
        actual = corruption_checksum(df)
        expected = 18
        self.assertEqual(actual,expected)

    def test_corruption_checksum_final(self):
        df = pd.read_csv("../p2_sheet.csv", header=None, delimiter="\t")
        actual = corruption_checksum(df)
        print(actual)


if __name__ == "__main__":
    unittest.main()