from src.Database.Query.SelectRegisteredCoursesQuery import SelectRegisteredCourses
import pytest

def test_numberOfAttributes():
    courses = SelectRegisteredCourses.queryAll((1,))
    
    assert(len(courses[0]) == 5)
    
def test_courseInformation():
    courses = SelectRegisteredCourses.queryAll((1,))
    
    assert(courses[0][0] == 1)
    assert(courses[0][1] == 'COSC303')
    assert(courses[0][2] == 'Numerical Analysis')
