import unittest
from stack_array import Stack
        
class TestLab2(unittest.TestCase):

    def test_init(self) -> None:
        stack = Stack(5)
        self.assertEqual(stack.items, [None]*5)
        self.assertEqual(stack.capacity, 5)

        stack = Stack(5, [1, 2])
        self.assertEqual(stack.items[0:2], [1, 2])
        self.assertEqual(stack.capacity, 5)

    def test_eq(self) -> None:
        stack1 = Stack(5)
        stack2 = Stack(5)
        stack3 = Stack(10)
        stack4 = Stack(5,[1, 2])
        self.assertEqual(stack1, stack2)
        self.assertNotEqual(stack1, stack3)
        self.assertNotEqual(stack1, stack4)
        self.assertFalse(stack1.__eq__(None))

    def test_repr(self) -> None:
        stack = Stack(5, [1, 2])
        self.assertEqual(stack.__repr__(), "Stack(5, [1, 2])")

# WRITE TESTS FOR STACK OPERATIONS - PUSH, POP, PEEK, etc.

    ### MORE TESTS ###

    ## PUSH ##
    # test push with normal case
    def test_push_01(self) -> None:
        testStack = Stack(10, [1, 2, 3])
        testStack.push('test')
        self.assertEqual(testStack, Stack(10, [1, 2, 3, 'test']))

    # test push with empty stack
    def test_push_02(self) -> None:
        testStack = Stack(10, [])
        testStack.push('test')
        self.assertEqual(testStack, Stack(10, ['test']))

    ## POP ##
    # test pop function with normal case
    def test_pop_01(self) -> None:
        testStack = Stack(10, [1, 2, 3])
        testStack.pop()
        self.assertEqual(testStack, Stack(10, [1, 2]))

    # test that pop function returns popped value with normal case
    def test_pop_02(self) -> None:
        testStack = Stack(10, [1, 2, 3])
        self.assertEqual(testStack.pop(), 3)

    # test multiple pops
    def test_pop_03(self) -> None:
        testStack = Stack(10, [1, 2, 3, 4])
        self.assertEqual(testStack.size(), 4)
        testStack.pop()
        testStack.pop()
        self.assertEqual(testStack, Stack(10, [1, 2]))
        self.assertEqual(testStack.size(), 2)

    # test that multiple pops returns correctly
    def test_pop_04(self) -> None:
        testStack = Stack(10, [1, 2, 3, 4])
        self.assertEqual(testStack.pop(), 4)
        self.assertEqual(testStack.pop(), 3)

    # test pop function with empty stack
    def test_pop_05(self) -> None:
        testStack = Stack(10, [])
        with self.assertRaises(IndexError):
            testStack.pop()


    ## PEEK ##
    # test peek for normal case
    def test_peek_01(self) -> None:
        testStack = Stack(10, [1, 2, 3, 4])
        self.assertEqual(testStack.peek(), 4)
        # check that testStack has not been modified from peek()
        self.assertEqual(testStack, Stack(10, [1, 2, 3, 4]))

    # test peek for empty stack
    def test_peek_02(self) -> None:
        testStack = Stack(10, [])
        with self.assertRaises(IndexError):
            testStack.peek()

    
    ## IS_EMPTY ## 
    # test is_empty for an empty stack
    def test_is_empty_01(self) -> None:
        testStack = Stack(10, [])
        self.assertTrue(testStack.is_empty())

    # test is_empty for non-empty stack
    def test_is_empty_02(self) -> None:
        testStack = Stack(10, [1, 2])
        self.assertFalse(testStack.is_empty())

    
    # IS_FULL ##
    # test is_full for a full stack
    def test_is_full_01(self) -> None:
        testStack = Stack(3, [1, 2, 3])
        self.assertTrue(testStack.is_full())

    # test is_full for a non-full stack
    def test_is_full_02(self) -> None:
        testStack = Stack(3, [1, 2])
        self.assertFalse(testStack.is_full())


    ## SIZE ##
    # test size for normal case
    def test_size_01(self) -> None:
        testStack = Stack(3, [1, 2, 3])
        self.assertEqual(testStack.size(), 3)

    # test size for empty stack
    def test_size_02(self) -> None:
        testStack = Stack(3, [])
        self.assertEqual(testStack.size(), 0)
    

if __name__ == '__main__': 
    unittest.main()
