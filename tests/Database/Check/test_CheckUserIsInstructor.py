from src.Database.Check.CheckUserIsInstructor import CheckUserIsInstructor
from tests.Database.DatabaseTestManager import DatabaseTestManager
import pytest


def test_RealUserId():
    DatabaseTestManager.startTest()
    
    userId = 3
    isStudent = CheckUserIsInstructor.check(userId)
    assert(isStudent == True) #Check there is an Instructor
    
    DatabaseTestManager.endTest()

def test_FakeUserId():
    DatabaseTestManager.startTest()

    userId = 1
    isStudent = CheckUserIsInstructor.check(userId)
    assert(isStudent == False) #Check there isn't an Instructor
    
    DatabaseTestManager.endTest()