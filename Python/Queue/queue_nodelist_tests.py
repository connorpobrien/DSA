import unittest
from queue_nodelist import *

class TestLab1(unittest.TestCase):

    def test_nodelist(self) -> None:
        q = Queue()
        self.assertEqual(q.rear, None)
        self.assertEqual(q.front, None)
        q.enqueue(1)
        self.assertEqual(q.rear, Node(1, None))
        self.assertEqual(q.front, None)
        q.enqueue(2)
        self.assertEqual(q.rear, Node(2, Node(1, None)))
        self.assertEqual(q.dequeue(),1)
        self.assertEqual(q.rear, None)
        self.assertEqual(q.front, Node(2, None))
        self.assertFalse(Node(1,None).__eq__(None))

    def test_repr(self) -> None:
        q = Queue()
        q.enqueue(1)
        self.assertEqual(q.__repr__(), "Queue(Node(1, None), None)")

    def test_eq(self) -> None:
        q1 = Queue()
        q1.enqueue(1)
        q1.enqueue(2)
        q2 = Queue()
        q2.enqueue(1)
        q2.enqueue(2)
        self.assertEqual(q1, q2)
        self.assertFalse(q1.__eq__(None))
        q1.dequeue()
        q2.dequeue()
        self.assertEqual(q1, q2)

    def test_queue_simple(self) -> None:
        q = Queue()
        q.enqueue(1)
        self.assertEqual(q.size(), 1)
        q.enqueue(2)
        q.enqueue(3)
        q.enqueue(4)
        q.enqueue(5)
        self.assertEqual(q.size(), 5)
        self.assertEqual(q.dequeue(), 1)
        self.assertEqual(q.dequeue(), 2)
        self.assertEqual(q.dequeue(), 3)
        self.assertEqual(q.dequeue(), 4)
        self.assertEqual(q.size(), 1)
        self.assertEqual(q.dequeue(), 5)


    ## MORE TESTS ##

    ## GET_ITEMS ##
    # test get_items after enqueue
    def test_get_items_01(self) -> None:
        q = Queue()
        self.assertEqual(q.get_items(), [])
        q.enqueue(1)
        self.assertEqual(q.get_items(), [1])
        q.enqueue(2)
        self.assertEqual(q.get_items(), [1, 2])
        q.enqueue(3)
        self.assertEqual(q.get_items(), [1, 2, 3])

    # test get_items with enqueue and dequeue
    def test_get_items_02(self) -> None:
        q = Queue()
        self.assertEqual(q.get_items(), [])
        q.enqueue(1)
        self.assertEqual(q.get_items(), [1])
        q.enqueue(2)
        self.assertEqual(q.get_items(), [1, 2])
        q.enqueue(3)
        self.assertEqual(q.get_items(), [1, 2, 3])
        q.dequeue()
        self.assertEqual(q.get_items(), [2, 3])
        q.enqueue(4)
        self.assertEqual(q.get_items(), [2, 3, 4])
        q.dequeue()
        self.assertEqual(q.get_items(), [3, 4])
        q.enqueue(5)
        self.assertEqual(q.get_items(), [3, 4, 5])
        q.dequeue()
        self.assertEqual(q.get_items(), [4, 5])
        q.dequeue()
        self.assertEqual(q.get_items(), [5])
        q.dequeue()
        self.assertEqual(q.get_items(), [])


    ## IS_EMPTY ##
    # test is_empty with enqueue
    def test_is_empty_01(self) -> None:
        q = Queue()
        self.assertTrue(q.is_empty())
        q.enqueue(1)
        self.assertFalse(q.is_empty())

    # test is_empty with enqueue and dequeue
    def test_is_empty_02(self) -> None:
        q = Queue()
        self.assertTrue(q.is_empty())
        q.enqueue(1)
        self.assertFalse(q.is_empty())
        q.enqueue(2)
        self.assertFalse(q.is_empty())
        q.dequeue()
        self.assertFalse(q.is_empty())
        q.enqueue(3)
        q.enqueue(4)
        self.assertFalse(q.is_empty())
        q.dequeue()
        self.assertFalse(q.is_empty())
        q.dequeue()
        self.assertFalse(q.is_empty())
        q.dequeue()
        self.assertTrue(q.is_empty())


    ## ENQUEUE ##
    # test enqueue for an empty self.rear
    def test_enque_01(self) -> None:
        q = Queue()
        self.assertEqual(q.rear, None)
        self.assertEqual(q.size(), 0)
        q.enqueue(1)
        self.assertEqual(q.rear, Node(1, None))
        self.assertEqual(q.size(), 1)

    # test enqueue for a non-empty self.rear (multiple enqueues)
    def test_enqueue_02(self) -> None:
        q = Queue()
        self.assertEqual(q.rear, None)
        self.assertEqual(q.size(), 0)
        q.enqueue(1)
        self.assertEqual(q.rear, Node(1, None))
        self.assertEqual(q.size(), 1)
        q.enqueue(2)
        self.assertEqual(q.rear, Node(2, Node(1, None)))
        self.assertEqual(q.size(), 2)
        q.enqueue(3)
        self.assertEqual(q.rear, Node(3, Node(2, Node(1, None))))
        self.assertEqual(q.size(), 3)


    ## DEQUEUE ##
    # test dequeue with items in q.front
    def test_dequeue_01(self) -> None:
        q = Queue()
        self.assertEqual(q.rear, None)

        # manually set q.front for test
        q.front = Node(1, Node(2, None))

        self.assertEqual(q.dequeue(), 1)
        self.assertEqual(q.front, Node(2, None))

        self.assertEqual(q.dequeue(), 2)
        self.assertEqual(q.front, None)

    # test dequeue with iems in both self.front and self.rear
    def test_dequeue_02(self) -> None:
        q = Queue()
        self.assertEqual(q.rear, None)

        # manually set q.front for test
        q.front = Node(1, Node(2, None))

        # manually set q.rear for test
        q.rear = Node(4, Node(3, None))

        self.assertEqual(q.dequeue(), 1)
        self.assertEqual(q.rear, Node(4, Node(3, None)))
        self.assertEqual(q.front, Node(2, None))

        self.assertEqual(q.dequeue(), 2)
        self.assertEqual(q.rear, Node(4, Node(3, None)))
        self.assertEqual(q.front, None)

    # test dequeue after enqueue (items in self.rear must shift to self.front)
    def test_dequeue_03(self) -> None:
        q = Queue()
        self.assertEqual(q.rear, None)
        self.assertEqual(q.size(), 0)

        q.enqueue(1)
        self.assertEqual(q.rear, Node(1, None))
        self.assertEqual(q.size(), 1)

        q.enqueue(2)
        self.assertEqual(q.rear, Node(2, Node(1, None)))
        self.assertEqual(q.size(), 2)

        self.assertEqual(q.dequeue(), 1)
        self.assertEqual(q.front, Node(2, None))
        self.assertEqual(q.rear, None)
        self.assertEqual(q.size(), 1)

        q.enqueue(3)
        self.assertEqual(q.front, Node(2, None))
        self.assertEqual(q.rear, Node(3, None))
        self.assertEqual(q.size(), 2)

        self.assertEqual(q.dequeue(), 2)
        self.assertEqual(q.front, None)
        self.assertEqual(q.rear, Node(3, None))
        self.assertEqual(q.size(), 1)
        
        q.enqueue(4)
        self.assertEqual(q.front, None)
        self.assertEqual(q.rear, Node(4, Node(3, None)))
        self.assertEqual(q.size(), 2)

        q.enqueue(5)
        self.assertEqual(q.front, None)
        self.assertEqual(q.rear, Node(5, Node(4, Node(3, None))))
        self.assertEqual(q.size(), 3)

        self.assertEqual(q.dequeue(), 3)
        self.assertEqual(q.front, Node(4, Node(5, None)))
        self.assertEqual(q.rear, None)
        self.assertEqual(q.size(), 2)

        self.assertEqual(q.dequeue(), 4)
        self.assertEqual(q.front, Node(5, None))
        self.assertEqual(q.rear, None)
        self.assertEqual(q.size(), 1)

        self.assertEqual(q.dequeue(), 5)
        self.assertEqual(q.front, None)
        self.assertEqual(q.rear, None)
        self.assertEqual(q.size(), 0)

        with self.assertRaises(IndexError):
            q.dequeue()

    # test dequeue with empty queue
    def test_deque_04(self) -> None:
        q = Queue()
        self.assertEqual(q.rear, None)
        self.assertEqual(q.size(), 0)

        with self.assertRaises(IndexError):
            q.dequeue()


    ## SIZE ##
    # test size with enqueue and dequeue
    def test_size_01(self) -> None:
        q = Queue()
        self.assertEqual(q.size(), 0)
        q.enqueue(1)
        self.assertEqual(q.size(), 1)
        q.enqueue(2)
        self.assertEqual(q.size(), 2)
        q.dequeue()
        self.assertEqual(q.size(), 1)
        q.enqueue(3)
        self.assertEqual(q.size(), 2)
        q.enqueue(4)
        self.assertEqual(q.size(), 3)
        q.dequeue()
        self.assertEqual(q.size(), 2)
        q.dequeue()
        self.assertEqual(q.size(), 1)
        q.dequeue()
        self.assertEqual(q.size(), 0)
        

if __name__ == '__main__': 
    unittest.main()
