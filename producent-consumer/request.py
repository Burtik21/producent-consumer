from abc import ABC, abstractmethod

class Request(ABC):
    def __init__(self, priority):
        self.priority = priority

    def __lt__(self, other):
        return self.priority < other.priority

    @abstractmethod
    def process(self):
        """Zpracování požadavku - definováno v potomcích."""
        pass
