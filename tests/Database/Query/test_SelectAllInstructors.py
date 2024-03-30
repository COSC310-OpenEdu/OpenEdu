from src.Database.Query.SelectAllInstructors import SelectAllInstructors
from tests.Database.DatabaseTestManager import DatabaseTestManager
import pytest

def test_numberOfInstructors():
    DatabaseTestManager.startTest()
    
    instructorId, instructorName = SelectAllInstructors.queryAll()
    
    assert(len(instructorId) == 1)
    assert(len(instructorName) == 1)
    
    DatabaseTestManager.endTest()
    
def test_instructorId():
    DatabaseTestManager.startTest()
    
    instructorId, instructorName = SelectAllInstructors.queryAll()
    assert(instructorId[0] == 3)

    DatabaseTestManager.endTest()

    
def test_instructorName():
    DatabaseTestManager.startTest()
    
    instructorId, instructorName = SelectAllInstructors.queryAll()
    assert(instructorName[0] == 'Jim Bob')
    
    DatabaseTestManager.endTest()



    