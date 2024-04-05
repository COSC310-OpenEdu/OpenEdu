from src.Database.Update.DeleteAllSolutionsForAssignment import DeleteAllSolutionsForAssignment
from src.Database.Update.DeleteGradesForAssignment import DeleteGradesForAssignment
from src.Database.Update.DeleteAllQuestionsForAssignment import DeleteAllQuestionsForAssignment
from src.Database.Query.SelectQuestionsForAssignment import SelectQuestionsForAssignment

from src.Database.Check.CheckAssignmentCompletion import CheckAssignmentCompletion
from tests.Database.DatabaseTestManager import DatabaseTestManager
import pytest

def test_DeleteAllQuestionsForAssignment():
    DatabaseTestManager.startTest()
    
    DeleteGradesForAssignment.update((1, 1,))
    DeleteAllSolutionsForAssignment.update((1, 1,))
    DeleteAllQuestionsForAssignment.update((1,1,))
    assert(not SelectQuestionsForAssignment.queryAll((1,1,)))
    
    DatabaseTestManager.endTest()