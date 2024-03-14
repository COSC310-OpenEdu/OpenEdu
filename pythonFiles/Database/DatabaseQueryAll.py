from abc import ABC, abstractmethod


class DatabaseQuery(ABC):
    @classmethod
    @abstractmethod
    def queryAll(cls, dataTuple) -> list:
        pass