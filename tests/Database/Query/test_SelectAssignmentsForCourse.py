from src.Database.Query.SelectAssignmentsForCourse import SelectAssignmentsForCourse
import pytest

def test_numberOfAssignments():
    assignments = SelectAssignmentsForCourse.queryAll((1,))
    assert(len(assignments) == 2)