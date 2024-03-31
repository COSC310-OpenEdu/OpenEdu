from src.Database.Check.CheckAssignmentExists import CheckAssignmentExists
from tests.Database.DatabaseTestManager import DatabaseTestManager
import pytest


def test_AssignmentExists():
    DatabaseTestManager.startTest()
    
    courseId = 1
    assignmentId = 1
    exists = CheckAssignmentExists.check(courseId,assignmentId,)
    assert(exists == True) #Check assignment exists
    
    DatabaseTestManager.endTest()

def test_AssignmentDoesntExist():
    DatabaseTestManager.startTest()

    courseId = 0
    assignmentId = 0
    exists = CheckAssignmentExists.check(courseId,assignmentId,)
    assert(exists == False) #Check assignment doesnt exist
    
    DatabaseTestManager.endTest()