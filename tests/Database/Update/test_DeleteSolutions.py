from src.Database.Update.DeleteSolutions import DeleteSolutions
from src.Database.Update.DeleteGradesForAssignment import DeleteGradesForAssignment

from src.Database.Check.CheckAssignmentCompletion import CheckAssignmentCompletion
from tests.Database.DatabaseTestManager import DatabaseTestManager
import pytest

def test_DeleteSolutions():
    DatabaseTestManager.startTest()
    
    DeleteGradesForAssignment.update(1, 1,)
    DeleteSolutions.update(1, 1, 1,)
    assert(CheckAssignmentCompletion.check((1, 1, 1,)) == False)
    
    DatabaseTestManager.endTest()
    
