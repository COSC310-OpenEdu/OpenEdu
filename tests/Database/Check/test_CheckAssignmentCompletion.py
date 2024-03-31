from src.Database.Check.CheckAssignmentCompletion import CheckAssignmentCompletion
from tests.Database.DatabaseTestManager import DatabaseTestManager
import pytest


def test_AssignmentComplete():
    DatabaseTestManager.startTest()
    
    courseId = 1
    assignmentId = 1
    studentId = 1
    isComplete = CheckAssignmentCompletion.check(courseId,assignmentId,studentId,)
    assert(isComplete != False) #Check assignment is complete
    
    DatabaseTestManager.endTest()

def test_AssignmentIncomplete():
    DatabaseTestManager.startTest()

    courseId = 0
    assignmentId = 0
    studentId = 0
    isComplete = CheckAssignmentCompletion.check(courseId,assignmentId,studentId,)
    assert(isComplete == False) #Check assignment is complete
    
    DatabaseTestManager.endTest()