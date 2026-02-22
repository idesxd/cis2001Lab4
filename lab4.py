import time
from gettext import install
import matplotlib.pyplot as plt
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        if not self.head:
            self.head = Node(data)
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = Node(data)

    def remove_head(self):
        if self.head:
            self.head = self.head.next


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


sizes = range(1000, 20000, 1000)
array_times = []
linked_times = []

for size in sizes:
    array_times.append(time_remove_head_array(size))
    linked_times.append(time_remove_head_linked(size))


plt.plot(sizes, array_times, label="Array List (pop(0))")
plt.plot(sizes, linked_times, label="Linked List (remove head)")
plt.xlabel("List Size (N)")
plt.ylabel("Time (seconds)")
plt.title("Remove First Element Performance")
plt.legend()
plt.show()

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
    new_node = Node(-1)
    new_node.next = ll.head
    ll.head = new_node
    end = time.perf_counter()
    return end - start