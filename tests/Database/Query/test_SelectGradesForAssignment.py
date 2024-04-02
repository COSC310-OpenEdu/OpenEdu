from src.Database.Query.SelectGradesForAssignment import SelectGradesForAssignment
from tests.Database.DatabaseTestManager import DatabaseTestManager
import pytest


def test_gradesLength():
    DatabaseTestManager.startTest()
    
    courseId = 1
    assignmentId = 1
    studentId = 1
    grades = SelectGradesForAssignment.queryAll((courseId, assignmentId, studentId,))
    assert(len(grades) == 3) 
    
    DatabaseTestManager.endTest()
