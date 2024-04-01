from src.Database.Query.SelectRegisteredCoursesQuery import SelectRegisteredCourses
from tests.Database.DatabaseTestManager import DatabaseTestManager
import pytest

def test_numberOfAttributes():
    DatabaseTestManager.startTest()
    
    courses = SelectRegisteredCourses.queryAll((1,))
    assert(len(courses[0]) == 5)
    
    DatabaseTestManager.endTest()
    
def test_courseInformation():
    DatabaseTestManager.startTest()
    
    courses = SelectRegisteredCourses.queryAll((1,))
    assert(courses[0][0] == 1)
    assert(courses[0][1] == 'COSC303')
    assert(courses[0][2] == 'Numerical Analysis')
    
    DatabaseTestManager.endTest()
