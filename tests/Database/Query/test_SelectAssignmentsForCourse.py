from src.Database.Query.SelectAssignmentsForCourse import SelectAssignmentsForCourse
from tests.Database.DatabaseTestManager import DatabaseTestManager
import pytest

def test_numberOfAssignments():
    DatabaseTestManager.startTest()
    
    assignments = SelectAssignmentsForCourse.queryAll((1,))
    assert(len(assignments) == 2)
    
    DatabaseTestManager.endTest()
