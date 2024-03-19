from src.Database.Query.SelectCourseQueryAll import SelectCourseQueryAll
import pytest

def test_SelectCourseQueryAll_courseName():
    courseData = SelectCourseQueryAll.queryAll((None,))
    assert(courseData[0][1] == "COSC303")
    
def test_SelectCourseQueryAll_courseId():
    courseData = SelectCourseQueryAll.queryAll((None,))
    assert(courseData[0][0] == 1)   