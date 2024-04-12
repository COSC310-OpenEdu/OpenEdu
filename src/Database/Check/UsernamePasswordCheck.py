from src.Database.Check.DatabaseCheck import DatabaseCheck
from src.Database.DatabaseManager import DatabaseManager
import mysql

class UsernamePasswordCheck(DatabaseCheck):
    
    #
    #   Checks if a given username and password have a user associated to them
    #   Input:  dataTuple = (username, password)
    #                     = username and password being checked
    #   Ouput:  True is the user exists
    #           False otherwise
    #
    
    @classmethod
    def check(cls, dataTuple) -> bool:
        statement = "SELECT * FROM User WHERE username = %s AND password = %s"
        username, password = dataTuple;

        cursor = DatabaseManager.getDatabaseCursor();
        cursor.execute(statement, (username, password,))
        userData = cursor.fetchone()
        DatabaseManager.closeConnection();

        if userData is None:
            return False
        else:
            return True
