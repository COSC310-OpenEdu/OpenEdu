from src.Database.DatabaseManager import DatabaseManager
import mysql

class DatabaseTestManager():
        
    @classmethod
    def rollback(cls):
        connection = DatabaseManager.getDatabaseConnection()

        connection.rollback();