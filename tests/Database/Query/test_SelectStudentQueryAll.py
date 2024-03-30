from src.Database.Query.SelectStudentQueryAll import SelectStudentQueryAll
from tests.Database.DatabaseTestManager import DatabaseTestManager
import pytest

def test_SelectStudentQueryAll_valid():
    DatabaseTestManager.startTest()
    
    studentData = SelectStudentQueryAll.queryAll((None,))
    assert(studentData[0][0] == "James") #Check there is a Student
    
    DatabaseTestManager.endTest()
    
def test_SelectStudentQueryAll_invalid():
    DatabaseTestManager.startTest()
    
    studentData = SelectStudentQueryAll.queryAll((None,))
    assert(studentData[1][0] != "James") #Check there is a Student
    
    DatabaseTestManager.endTest()