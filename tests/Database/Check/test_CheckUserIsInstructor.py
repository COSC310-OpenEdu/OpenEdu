from src.Database.Check.CheckUserIsInstructor import CheckUserIsInstructor
import pytest


def test_RealUserId():
    userId = 3
    isStudent = CheckUserIsInstructor.check(userId)
    assert(isStudent == True) #Check there is an Instructor

def test_FakeUserId():
    userId = 1
    isStudent = CheckUserIsInstructor.check(userId)
    assert(isStudent == False) #Check there isn't an Instructor