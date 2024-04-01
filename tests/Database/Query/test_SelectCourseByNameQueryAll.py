from src.Database.Query.SelectCourseByNameQueryAll import SelectCourseQueryAll
from tests.Database.DatabaseTestManager import DatabaseTestManager
import pytest

def test_SelectCourseByNameQueryAll_courseName():
    DatabaseTestManager.startTest()
    
    courseData = SelectCourseQueryAll.queryAll(('303',))
    assert(courseData[0][1] == "COSC303")
    
    DatabaseTestManager.endTest()
    
def test_SelectCourseByNameQueryAll_courseId():
    DatabaseTestManager.startTest()
    
    courseData = SelectCourseQueryAll.queryAll(('303',))
    assert(courseData[0][0] == 1)
    
    DatabaseTestManager.endTest()
    
def test_SelectCourseByNameQueryAll_length():
    DatabaseTestManager.startTest()

    courseData = SelectCourseQueryAll.queryAll(('303',))
    assert(len(courseData) == 1)   
    
    DatabaseTestManager.endTest()