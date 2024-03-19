from src.Database.Query.SelectCoursesTaughtByIntructor import SelectCoursesTaughtByInstructor
import pytest


def test_Instructor():
    userId = 3
    StudentData = SelectCoursesTaughtByInstructor.queryAll(userId)
    assert(len(StudentData) == 4) #Make sure he teaches four courses