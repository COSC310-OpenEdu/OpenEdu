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