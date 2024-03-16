from src.Database.Query.SelectStudentQueryAll import SelectStudentQueryAll
import pytest

def test_SelectStudentQueryAll_valid():
    
    studentData = SelectStudentQueryAll.queryAll((None,))
    assert(studentData[0][0] == "James") #Check there is a Student
    
def test_SelectStudentQueryAll_invalid():
    studentData = SelectStudentQueryAll.queryAll((None,))
    assert(studentData[1][0] != "James") #Check there is a Student