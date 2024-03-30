from src.Database.Query.SelectAllInstructors import SelectAllInstructors
import pytest

def test_numberOfInstructors():
    instructorId, instructorName = SelectAllInstructors.queryAll()
    
    assert(len(instructorId) == 2)
    assert(len(instructorName) == 2)
    
def test_instructorId():
    instructorId, instructorName = SelectAllInstructors.queryAll()
    
    assert(instructorId[0] == 3)
    assert(instructorId[1] == 5)
    
def test_instructorName():
    instructorId, instructorName = SelectAllInstructors.queryAll()
    
    assert(instructorName[0] == 'Jim Bob')
    assert(instructorName[1] == 'Casey Truman')

    