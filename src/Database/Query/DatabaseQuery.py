from abc import ABC, abstractmethod

class DatabaseQuery(ABC):
    @classmethod
    @abstractmethod
    def query(cls, dataTuple) -> tuple:
        pass;