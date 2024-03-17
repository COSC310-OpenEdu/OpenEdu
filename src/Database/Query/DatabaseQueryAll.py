from abc import ABC, abstractmethod


class DatabaseQueryAll(ABC):
    @classmethod
    @abstractmethod
    def queryAll(cls, dataTuple) -> list:
        pass