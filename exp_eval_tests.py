# Start of unittest - add to completely test functions in exp_eval

import unittest
from exp_eval import *

class test_expressions(unittest.TestCase):
    def test_postfix_eval_01(self):
        self.assertAlmostEqual(postfix_eval("2 3 * 5 7 + + 8 +"), 26)

    def test_postfix_eval_02(self):
        try:
            postfix_eval("blah")
            self.fail()
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Invalid token")

    def test_postfix_eval_03(self):
        try:
            postfix_eval("4 +")
            self.fail()
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Insufficient operands")

    def test_postfix_eval_04(self):
        try:
            postfix_eval("1 2 3 +")
            self.fail()
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Too many operands")
    def test_operators(self):
        self.assertAlmostEqual(postfix_eval("3 2 -"), 1)
        self.assertAlmostEqual(postfix_eval("3 2 *"), 6)
        self.assertAlmostEqual(postfix_eval("3 2 /"), 1.5)
        self.assertAlmostEqual(postfix_eval("3 2 **"), 9)
        self.assertAlmostEqual(postfix_eval("0 2 /"), 0)
        with self.assertRaises(PostfixFormatException):
            try:
                postfix_eval("2 0 /")
 




    def test_postfix_float(self):
        self.assertAlmostEqual(postfix_eval("2.5 2 +"), 4.5)

    def test_prefix_eval(self):
        self.assertAlmostEqual("2 2 +", prefix_to_postfix("+ 2 2"))

if __name__ == "__main__":
    unittest.main()
