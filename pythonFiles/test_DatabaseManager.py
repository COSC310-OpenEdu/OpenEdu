from DatabaseManager import DatabaseManager
import pytest


def test_ViewStudents():
    database = DatabaseManager()
    database.viewStudents()
    
    # Print Result-set
    #for (firstName, lastName) in database.cur:
        #print(f"First Name: {firstName}, Last Name: {lastName}")
        
    row = database.cur.fetchone()
    assert(row[0] == "James")
    
    database.closeConnection()


