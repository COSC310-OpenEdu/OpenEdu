from abc import ABC, abstractmethod

#
#   A database call that updates the database tables
#   These functions should return true if successful
#

class DatabaseUpdate(ABC):
    @classmethod
    @abstractmethod
    def update(cls, dataTuple) -> bool:
        pass;
    