from abc import ABC, abstractmethod

class DatabaseUpdate(ABC):
    @classmethod
    @abstractmethod
    def update(cls, dataTuple) -> bool:
        pass;
    