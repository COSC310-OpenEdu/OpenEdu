from src.Database.Query.SelectCourseQueryAll import SelectCourseQueryAll
from tests.Database.DatabaseTestManager import DatabaseTestManager
import pytest

def test_SelectCourseQueryAll_courseName():
    DatabaseTestManager.startTest()
    
    courseData = SelectCourseQueryAll.queryAll((None,))
    assert(courseData[0][1] == "COSC303")
    
    DatabaseTestManager.endTest()
    
    
def test_SelectCourseQueryAll_courseId():
    DatabaseTestManager.startTest()
    
    courseData = SelectCourseQueryAll.queryAll((None,))
    assert(courseData[0][0] == 1)   
    
    DatabaseTestManager.endTest()
    
    
def test_SelectCourseQueryAll_searchTerm_courseName():
    DatabaseTestManager.startTest()
    
    courseData = SelectCourseQueryAll.queryAll(('404',))
    assert(courseData[0][1] == "COSC404")
    
    DatabaseTestManager.endTest()
 
    
def test_SelectCourseQueryAll_searchTerm_id():
    DatabaseTestManager.startTest()
    
    courseData = SelectCourseQueryAll.queryAll(('404',))
    assert(courseData[0][0] == 4)   
    
    DatabaseTestManager.endTest()