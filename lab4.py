import time
import matplotlib.pyplot as plt



class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return

        self.tail.next = new_node
        self.tail = new_node

    def remove_head(self):
        if self.head is not None:
            self.head = self.head.next
            if self.head is None:
                self.tail = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

        if self.tail is None:
            self.tail = new_node




def average_time(func, n, trials=50):
    total = 0
    for _ in range(trials):
        total += func(n)
    return total / trials




def time_remove_head_array(n):
    arr = list(range(n))
    start = time.perf_counter()
    arr.pop(0)
    end = time.perf_counter()
    return end - start


def time_remove_head_linked(n):
    ll = LinkedList()
    for i in range(n):
        ll.append(i)

    start = time.perf_counter()
    ll.remove_head()
    end = time.perf_counter()
    return end - start


def time_insert_beginning_array(n):
    arr = list(range(n))
    start = time.perf_counter()
    arr.insert(0, -1)
    end = time.perf_counter()
    return end - start


def time_insert_beginning_linked(n):
    ll = LinkedList()
    for i in range(n):
        ll.append(i)

    start = time.perf_counter()
    ll.insert_at_beginning(-1)
    end = time.perf_counter()
    return end - start
