from src.Database.Check.CheckUserIsStudent import CheckUserIsStudent
import pytest


def test_RealUserId():
    userId = 1
    isStudent = CheckUserIsStudent.check(userId)
    assert(isStudent == True) #Check there is a Student

def test_FakeUserId():
    userId = 3
    isStudent = CheckUserIsStudent.check(userId)
    assert(isStudent == False) #Check there isn't a Student