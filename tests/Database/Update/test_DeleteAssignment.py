from src.Database.Update.DeleteAssignment import DeleteAssignment
from src.Database.Update.DeleteGradesForAssignment import DeleteGradesForAssignment
from src.Database.Update.DeleteAllSolutionsForAssignment import DeleteAllSolutionsForAssignment

from src.Database.Check.CheckAssignmentExists import CheckAssignmentExists
from tests.Database.DatabaseTestManager import DatabaseTestManager
import pytest

def test_DeleteAssignment():
    DatabaseTestManager.startTest()
    
    DeleteGradesForAssignment.update(1, 1,)
    DeleteAllSolutionsForAssignment.update(1, 1,)
    DeleteAssignment.update(1, 1,)
    assert(CheckAssignmentExists.check((1, 1,)) == False)
    
    DatabaseTestManager.endTest()
    
