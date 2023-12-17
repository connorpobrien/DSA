import unittest
from stack_nodelist import *
        
class TestLab2(unittest.TestCase):

    def test_node_init(self) -> None:
        node1 = Node(1, None)
        self.assertEqual(node1.value, 1)
        self.assertEqual(node1.next, None)

        node2 = Node(2, node1)
        self.assertEqual(node2.value, 2)
        self.assertEqual(node2.next, node1)

    def test_node_eq(self) -> None:
        node1a = Node(1, None)
        node1b = Node(1, None)
        node2a = Node(2, node1a)
        node2b = Node(2, node1b)

        self.assertEqual(node1a, node1b)
        self.assertNotEqual(node1a, node2a)
        self.assertEqual(node2a, node2b)
        node1a = Node(3, None)
        self.assertNotEqual(node1a, node1b)

        self.assertFalse(node1a.__eq__(None))

    def test_node_repr(self) -> None:
        node = Node(2, Node(1, None))
        self.assertEqual(node.__repr__(), "Node(2, Node(1, None))")

    def test_stack_init(self) -> None:
        stack = Stack()
        self.assertEqual(stack.top, None)

        init_stack = Node(2, Node(1, None))
        stack = Stack(init_stack)
        self.assertEqual(stack.top, init_stack)

    def test_stack_eq(self) -> None:
        stack1 = Stack()
        stack2 = Stack()
        init_stack = Node(2, Node(1, None))
        stack4 = Stack(init_stack)
        self.assertEqual(stack1, stack2)
        self.assertNotEqual(stack1, stack4)
        self.assertFalse(stack1.__eq__(None))

    def test_stack_repr(self) -> None:
        init_stack = Node(2, Node(1, None))
        stack = Stack(init_stack)
        self.assertEqual(stack.__repr__(), "Stack(Node(2, Node(1, None)))")

# WRITE TESTS FOR STACK OPERATIONS - PUSH, POP, PEEK, etc.

    ## IS_EMPTY ##
    # test is_empty for a non-empty stack
    def test_is_empty_01(self) -> None:
        testStack = Stack(Node(45, Node(56, None)))
        self.assertFalse(testStack.is_empty())

    # test is_empty for an empty stack
    def test_is_empty_02(self) -> None:
        testStack = Stack(None)
        self.assertTrue(testStack.is_empty())


    ## SIZE ##
    # test size for normal case
    def test_size_01(self) -> None:
        testStack = Stack(Node(45, Node(56, Node(100, None))))
        self.assertEqual(testStack.size(), 3)

    # test size for empty stack
    def test_size_02(self) -> None:
        testStack = Stack(None)
        self.assertEqual(testStack.size(), 0)

    
    ## PUSH ##
    # test push for nomal case
    def test_push_01(self) -> None:
        testStack = Stack(Node(45, Node(56, None)))
        testStack.push('test')
        self.assertEqual(testStack, Stack(Node('test', Node(45, Node(56, None)))))

    # test push for empty stack 
    def test_push_02(self) -> None:
        testStack = Stack(None)
        testStack.push('test')
        self.assertEqual(testStack, Stack(Node('test', None)))


    ## POP ##
    # test pop for normal case
    def test_pop_01(self) -> None:
        testStack = Stack(Node(45, Node(56, Node(100, None))))
        testStack.pop()
        self.assertEqual(testStack, Stack(Node(56, Node(100, None))))

    # test that pop returns correct value for normal case
    def test_pop_02(self) -> None:
        testStack = Stack(Node(45, Node(56, Node(100, None))))
        self.assertEqual(testStack.pop(), 45)

    # test pop for an empty stack
    def test_pop_03(self) -> None:
        testStack = Stack(None)
        with self.assertRaises(IndexError):
            testStack.pop()

    
    ## PEEK ##
    # test peek for normal case
    def test_peek_01(self) -> None:
        testStack = Stack(Node(45, Node(56, Node(100, None))))
        self.assertEqual(testStack.peek(), 45)

    # test peek for an empty stack
    def test_peek_02(self) -> None:
        testStack = Stack(None)
        with self.assertRaises(IndexError):
            testStack.peek()
    
    
if __name__ == '__main__': 
    unittest.main()
