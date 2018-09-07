import unittest
from stack import Stack

class TestStack(unittest.TestCase):
    def testCreate(self):
        stack = Stack()
        self.assertTrue(stack.isEmpty())
