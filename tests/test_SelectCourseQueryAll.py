from src.Database.Query.SelectCourseQueryAll import SelectCourseQueryAll
import pytest

def test_SelectCourseQueryAll_courseName():
    courseData = SelectCourseQueryAll.queryAll((None,))
    assert(courseData[0][1] == "COSC303")
    
def test_SelectCourseQueryAll_courseId():
    courseData = SelectCourseQueryAll.queryAll((None,))
    assert(courseData[0][0] == 1)   
    
def test_SelectCourseQueryAll_searchTerm_courseName():
    courseData = SelectCourseQueryAll.queryAll(('404',))
    assert(courseData[0][1] == "COSC404")
    
def test_SelectCourseQueryAll_searchTerm_id():
    courseData = SelectCourseQueryAll.queryAll(('404',))
    assert(courseData[0][0] == 4)   