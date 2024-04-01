from src.Database.Query.SelectSolutionsForCourse import SelectSolutionsForCourse
from tests.Database.DatabaseTestManager import DatabaseTestManager
import pytest


def test_solutionsLength():
    DatabaseTestManager.startTest()
    
    courseId = 1
    solutions = SelectSolutionsForCourse.queryAll((courseId,))
    assert(len(solutions) == 6) 
    
    DatabaseTestManager.endTest()