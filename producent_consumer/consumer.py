import time
from producent_consumer.linked_list_queue import LinkedListQueue

class Consumer:
    def __init__(self, queue: LinkedListQueue, log):
        self.queue = queue
        self.log = log  # Funkce pro zápis logu

    def run(self):
        """Konzument zpracovává požadavky z fronty."""
        while True:
            request = self.queue.dequeue()
            if request:
                self.log(f"Processing request: {type(request).__name__}")
                request.process()
            else:
                time.sleep(0.1)
