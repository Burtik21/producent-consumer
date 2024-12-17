from producent_consumer.request_factory import RequestFactory
from producent_consumer.linked_list_queue import LinkedListQueue

class Producer:
    def __init__(self, queue: LinkedListQueue, log):
        self.queue = queue
        self.log = log  # Funkce pro zápis logu

    def run(self):
        """Producent čeká na vstup od uživatele a přidává požadavky do fronty."""
        while True:
            user_input = input("Enter request (e.g., 'deal 1', 'end'): ")
            try:
                request = RequestFactory.create_request(user_input)
                self.queue.enqueue(request)
                self.log(f"Added request: {type(request).__name__}")
            except ValueError as e:
                self.log(f"Error: {e}")
                print(e)
