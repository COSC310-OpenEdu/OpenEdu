from src.Database.Check.CheckSubmissionIsGraded import CheckSubmissionIsGraded
from tests.Database.DatabaseTestManager import DatabaseTestManager
import pytest


def test_SubmissionIsGraded():
    DatabaseTestManager.startTest()
    
    courseId = 1
    assignmentId = 1
    studentId = 1
    exists = CheckSubmissionIsGraded.check((courseId,assignmentId, studentId,))
    assert(exists == True) #Check assignment exists
    
    DatabaseTestManager.endTest()

def test_SubmissionNotGraded():
    DatabaseTestManager.startTest()

    courseId = 0
    assignmentId = 0
    studentId = 0
    exists = CheckSubmissionIsGraded.check((courseId,assignmentId,studentId,))
    assert(exists == False) #Check assignment doesnt exist
    
    DatabaseTestManager.endTest()