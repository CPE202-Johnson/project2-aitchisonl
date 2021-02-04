
import unittest

# Use the imports below to test either your array-based stack
# or your link-based version
from stack_array import Stack
#from stack_linked import Stack

class TestLab2(unittest.TestCase):
    def test_simple(self):
        stack = Stack(5)
        stack.push(0)
        self.assertFalse(stack.is_empty())
        self.assertFalse(stack.is_full())
        self.assertEqual(stack.size(),1)
    def test_size(self):
        stack = Stack(5)
        stack.push(1)
        stack.push(2)

        self.assertEqual(stack.size(), 2)
        
    def test_pop(self):
        stack = Stack(5)
        stack.push(3)
        stack.push(1)
        stack.push(2)
        stack.push(3)
        stack.pop()
        stack.push(1)

        self.assertEqual(stack.pop(), 1)
    def test_pop_error(self):
        stack = Stack(5)
        with self.assertRaises(IndexError):
            stack.pop()
    def test_push_error(self):
        stack = Stack(2)
        stack.push(1)
        stack.push(2)
        with self.assertRaises(IndexError):
            stack.push(3)
    def test_peek(self):
        stack = Stack(2)
        stack.push(3)
        self.assertEqual(stack.peek(), 3)
    def test_peek_error(self):
        stack = Stack(3)
        with self.assertRaises(IndexError):
            stack.peek()
    def test_is_full(self):
        stack = Stack(5)
        self.assertFalse(stack.is_full())
        stack.push(11)
        stack.push(12)
        stack.push(13)
        stack.push(14)
        stack.push(15)
        self.assertTrue(stack.is_full())
        stack.pop()
        self.assertFalse(stack.is_full())

if __name__ == '__main__': 
    unittest.main()
