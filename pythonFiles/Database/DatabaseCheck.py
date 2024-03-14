from abc import ABC, abstractmethod

class DatabaseCheck(ABC):
    @classmethod
    @abstractmethod
    def check(cls, dataTuple) -> bool:
        pass;