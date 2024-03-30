from src.Database.Query.SelectCoursesTaughtByIntructor import SelectCoursesTaughtByInstructor
from tests.Database.DatabaseTestManager import DatabaseTestManager
import pytest


def test_Instructor():
    DatabaseTestManager.startTest()
    
    userId = 3
    StudentData = SelectCoursesTaughtByInstructor.queryAll(userId)
    assert(len(StudentData) == 4) #Make sure he teaches four courses
    
    DatabaseTestManager.endTest()