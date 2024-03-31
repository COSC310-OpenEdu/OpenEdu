from src.Database.Update.DeleteAssignment import DeleteAssignment


from src.Database.Check.CheckAssignmentExists import CheckAssignmentExists
from tests.Database.DatabaseTestManager import DatabaseTestManager
import pytest

def test_DeleteAssignment():
    DatabaseTestManager.startTest()
    
    
    DeleteAssignment.update((1, 2,))
    assert(CheckAssignmentExists.check((1, 2,)) == False)
    
    DatabaseTestManager.endTest()
    
