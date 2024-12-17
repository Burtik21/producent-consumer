import time
from threading import Thread
from request import Request
from linked_list_queue import LinkedListQueue
from request_factory import RequestFactory

class GameManager:
    def __init__(self):
        self.queue = LinkedListQueue()

    def producer(self):
        while True:
            user_input = input("Enter request (e.g., 'deal 1', 'end'): ")
            try:
                request = RequestFactory.create_request(user_input)
                self.queue.enqueue(request)
                print(f"Added request: {type(request).__name__}")
            except ValueError as e:
                print(e)

    def consumer(self):
        while True:
            request = self.queue.dequeue()
            if request:
                request.process()
            else:
                time.sleep(0.1)

    def run(self):
        producer_thread = Thread(target=self.producer)
        consumer_thread = Thread(target=self.consumer)

        producer_thread.start()
        consumer_thread.start()

        producer_thread.join()
        consumer_thread.join()
