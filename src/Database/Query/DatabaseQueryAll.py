from abc import ABC, abstractmethod

#
#   A type of database call the returns multiple rows in the form of a list
#   dataTuple is used to pass information into the query
#

class DatabaseQueryAll(ABC):
    @classmethod
    @abstractmethod
    def queryAll(cls, dataTuple) -> list:
        pass