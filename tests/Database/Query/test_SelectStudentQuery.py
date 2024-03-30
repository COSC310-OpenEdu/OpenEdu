from src.Database.Query.SelectStudentQuery import SelectStudentQuery
import pytest

def test_selectCourseQuery_valid():
    userId = 1
    
    studentData = SelectStudentQuery.query((userId,))
    assert(studentData[1] == "James")
    
def test_selectCourseQuery_invalid():
    userId = 1
    
    studentData = SelectStudentQuery.query((userId,))
    assert(studentData[1] != "NotJames")
    
def test_selectCourseQuery_nonIntegerId():
    userId = 'Cat'
    
    studentData = SelectStudentQuery.query((userId,))
    assert(studentData is None)