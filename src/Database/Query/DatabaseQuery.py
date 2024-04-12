from abc import ABC, abstractmethod

#
#   A type of database call the returns a single row
#   dataTuple is used to pass information into the query
#

class DatabaseQuery(ABC):
    @classmethod
    @abstractmethod
    def query(cls, dataTuple) -> tuple:
        pass;