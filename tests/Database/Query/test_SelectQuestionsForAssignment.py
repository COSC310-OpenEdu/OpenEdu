from src.Database.Query.SelectQuestionsForAssignment import SelectQuestionsForAssignment
from tests.Database.DatabaseTestManager import DatabaseTestManager
import pytest


def test_questionsLength():
    DatabaseTestManager.startTest()
    
    courseId = 1
    assignmentId = 1
    questions = SelectQuestionsForAssignment.queryAll(courseId, assignmentId,)
    assert(len(questions) == 3) 
    
    DatabaseTestManager.endTest()