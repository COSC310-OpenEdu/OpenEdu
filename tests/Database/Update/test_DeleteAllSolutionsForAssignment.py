from src.Database.Update.DeleteAllSolutionsForAssignment import DeleteAllSolutionsForAssignment
from src.Database.Update.DeleteGradesForAssignment import DeleteGradesForAssignment

from src.Database.Check.CheckAssignmentCompletion import CheckAssignmentCompletion
from tests.Database.DatabaseTestManager import DatabaseTestManager
import pytest

def test_DeleteAllSolutionsForAssignment():
    DatabaseTestManager.startTest()
    
    DeleteGradesForAssignment.update((1, 1,))
    DeleteAllSolutionsForAssignment.update((1, 1,))
    assert(CheckAssignmentCompletion.check((1, 1, 1,)) == False)
    
    DatabaseTestManager.endTest()
    
