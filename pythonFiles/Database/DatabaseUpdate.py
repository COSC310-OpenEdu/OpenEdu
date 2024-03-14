from abc import ABC, abstractmethod

class DatabaseQuery(ABC):
    @classmethod
    @abstractmethod
    def update(cls, dataTuple) -> bool:
        pass;