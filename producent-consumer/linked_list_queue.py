from threading import Lock  # Import Lock z modulu threading

class Node:
    def __init__(self, request):
        self.request = request
        self.next = None


class LinkedListQueue:
    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super(LinkedListQueue, cls).__new__(cls)
            cls._instance._init_queue()
        return cls._instance

    def _init_queue(self):
        self.head = None
        self.tail = None
        self.lock = Lock()

    def enqueue(self, request):
        with self.lock:
            new_node = Node(request)
            if self.tail:
                self.tail.next = new_node
            self.tail = new_node
            if not self.head:
                self.head = new_node

    def dequeue(self):
        with self.lock:
            if not self.head:
                return None
            request = self.head.request
            self.head = self.head.next
            if not self.head:
                self.tail = None
            return request

    def is_empty(self):
        with self.lock:
            return self.head is None
