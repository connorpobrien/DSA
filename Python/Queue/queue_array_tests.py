import unittest
from queue_array import Queue

class TestLab1(unittest.TestCase):

    def test_array(self) -> None:
        q = Queue(5)
        self.assertEqual(q.items, [None, None, None, None, None])
        self.assertEqual(q.get_items(), [])
        q.enqueue(1)
        self.assertEqual(q.items, [1, None, None, None, None])
        q.enqueue(2)
        self.assertEqual(q.items, [1, 2, None, None, None])

    def test_init_eq(self) -> None:
        with self.assertRaises(IndexError):
            q = Queue(5, [1, 2, 3, 4, 5, 6])
        q1 = Queue(5, [1, 2, 3, 4])
        self.assertEqual(q1.get_items(), [1, 2, 3, 4])
        q2 = Queue(5, [1, 2, 3, 4])
        self.assertEqual(q1, q2)

    def test_init_eq2(self) -> None:
        q1 = Queue(5, [1, 2, 3, 4, 5])
        q2 = Queue(5, [1, 2, 3, 4, 5])
        self.assertFalse(q1.__eq__(None))
        self.assertEqual(q1, q2)

    def test_repr(self) -> None:
        q1 = Queue(5, [])
        self.assertEqual(q1.__repr__(), "Queue(5, [])")

    def test_queue_simple(self) -> None:
        q = Queue(5)
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

    ## IS_EMPTY ##
    # test is_empty with an empty queue
    def test_is_empty_01(self) -> None:
        q = Queue(5)
        self.assertTrue(q.is_empty())

    # test is_empty with a non-empty queue
    def test_is_empty_02(self) -> None:
        q = Queue(5, [1, 2, 3])
        self.assertFalse(q.is_empty())


    ## IS_FULL ##
    # test is_full with a full queue
    def test_is_full_02(self) -> None:
        q = Queue(3, [1, 2, 3])
        self.assertTrue(q.is_full())

    # test is_full with a non-full queue
    def test_is_full_01(self) -> None:
        q = Queue(3, [1, 2, 3])
        self.assertTrue(q.is_full())

    
    ## SIZE ##
    # test size with empty queue
    def test_size_01(self) -> None:
        q = Queue(5)
        self.assertEqual(q.size(), 0)

    # test size with a normal queue
    def test_size_02(self) -> None:
        q = Queue(5, [1, 2, 3])
        self.assertEqual(q.size(), 3)

    # tets size with a full queue
    def test_size_03(self) -> None:
        q = Queue(5, [1, 2, 3, 4, 5])
        self.assertEqual(q.size(), 5)

    
    ## ENQUEUE ##
    # test enque to an empty queue
    def test_enque_01(self) -> None:
        q = Queue(5)
        q.enqueue(10)
        self.assertEqual(q.size(), 1)
        self.assertEqual(q.get_items(), [10])

    # test enque in normal case
    def test_enque_02(self) -> None:
        q = Queue(5, [1, 2])
        q.enqueue(10)
        self.assertEqual(q.size(), 3)
        self.assertEqual(q.get_items(), [1, 2, 10])

    # test enque for an already full queue
    def test_enque_03(self) -> None:
        q = Queue(3, [1, 2, 3])
        with self.assertRaises(IndexError):
            q.enqueue(10)


    ## DEQUE ##
    # test dequeue in normal case
    def test_dequeue_01(self) -> None:
        q = Queue(5, [1, 2, 3])
        q.dequeue()
        self.assertEqual(q.size(), 2)
        self.assertEqual(q.get_items(), [2, 3])

    # test deque for full queue
    def test_dequeue_02(self) -> None:
        q = Queue(3, [1, 2, 3])
        q.dequeue()
        self.assertEqual(q.size(), 2)
        self.assertEqual(q.get_items(), [2, 3])

    # test deque for empty queue
    def test_dequeue_03(self) -> None:
        q = Queue(5)
        with self.assertRaises(IndexError):
            q.dequeue()

if __name__ == '__main__':
    unittest.main()
