from abc import ABC, abstractmethod
#
#   A type of database call the returns a boolean based on an input
#
class DatabaseCheck(ABC):
    @classmethod
    @abstractmethod
    def check(cls, dataTuple) -> bool:
        pass;
