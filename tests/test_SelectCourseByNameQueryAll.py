from src.Database.Query.SelectCourseByNameQueryAll import SelectCourseQueryAll
import pytest

def test_SelectCourseByNameQueryAll_courseName():
    courseData = SelectCourseQueryAll.queryAll(('303',))
    assert(courseData[0][1] == "COSC303")
    
def test_SelectCourseByNameQueryAll_courseId():
    courseData = SelectCourseQueryAll.queryAll(('303',))
    assert(courseData[0][0] == 1)
    
def test_SelectCourseByNameQueryAll_length():
    courseData = SelectCourseQueryAll.queryAll(('303',))
    
    assert(len(courseData) == 1)   