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
sizes = range(1000, 20000, 1000)

array_remove_times = []
linked_remove_times = []

array_insert_times = []
linked_insert_times = []

print("Collecting timing data...")

for size in sizes:
    array_remove_times.append(average_time(time_remove_head_array, size))
    linked_remove_times.append(average_time(time_remove_head_linked, size))

    array_insert_times.append(average_time(time_insert_beginning_array, size))
    linked_insert_times.append(average_time(time_insert_beginning_linked, size))

print("Done. Generating graphs...")

plt.figure()
plt.plot(sizes, array_remove_times, label="Array List pop(0)")
plt.plot(sizes, linked_remove_times, label="Linked List remove head")
plt.xlabel("List Size (N)")
plt.ylabel("Time (seconds)")
plt.title("Remove First Element Performance")
plt.legend()
plt.show()


plt.figure()
plt.plot(sizes, array_insert_times, label="Array List insert(0)")
plt.plot(sizes, linked_insert_times, label="Linked List insert at beginning")
plt.xlabel("List Size (N)")
plt.ylabel("Time (seconds)")
plt.title("Insert at Beginning Performance")
plt.legend()
plt.show()