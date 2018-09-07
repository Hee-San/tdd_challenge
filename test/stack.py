import unittest
from stack import Stack

class TestStack(unittest.TestCase):
    def __init__(self):
        self.stack = Stack()
    def testCreate(self):
        self.assertTrue(self.stack.isEmpty())
    def testPushAndTop(self):
        self.stack.push(1)
        self.assertEqual(1, self.stack.top())
