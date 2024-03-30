from src.Database.DatabaseManager import DatabaseManager
import mysql

class DatabaseTestManager():
    
    @classmethod
    def startTransation(cls):
        connection = DatabaseManager.getDatabaseConnection()
        
        connection.start_transaction()
        
    @classmethod
    def rollback(cls):
        connection = DatabaseManager.getDatabaseConnection()

        connection.rollback()
    
    # Sets up environment for testing
    @classmethod
    def startTest(cls):
        DatabaseManager.test = True
        cls.startTransation()
    
    
    # Reverts all changes from tests
    @classmethod
    def endTest(cls):
        DatabaseManager.test = False
        cls.rollback()
        cls.rollback()
        