from src.Database.Query.SelectInstructorsForCourse import SelectInstructorsForCourse
import pytest

def test_instructorForCourse1():
    instructor = SelectInstructorsForCourse.queryAll((1,));
    
    assert(instructor[0][0] == 3)
    assert(instructor[0][1] == 'Jim')
    assert(instructor[0][2] == 'Bob')