from src.Database.Query.SelectStudentQuery import SelectStudentQuery
from tests.Database.DatabaseTestManager import DatabaseTestManager
import pytest

def test_selectCourseQuery_valid():
    DatabaseTestManager.startTest()
    
    userId = 1
    studentData = SelectStudentQuery.query((userId,))
    assert(studentData[1] == "James")
    
    DatabaseTestManager.endTest()
    
def test_selectCourseQuery_invalid():
    DatabaseTestManager.startTest()
    
    userId = 1    
    studentData = SelectStudentQuery.query((userId,))
    assert(studentData[1] != "NotJames")
    
    DatabaseTestManager.endTest()
    
def test_selectCourseQuery_nonIntegerId():
    DatabaseTestManager.startTest()
    
    userId = 'Cat'
    studentData = SelectStudentQuery.query((userId,))
    assert(studentData is None)
    
    DatabaseTestManager.endTest()