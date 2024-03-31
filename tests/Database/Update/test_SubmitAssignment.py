from src.Database.Update.SubmitAssignment import SubmitAssignment
from src.Database.Update.DeleteSolutions import DeleteSolutions
from src.Database.Update.DeleteGradesForAssignment import DeleteGradesForAssignment

from src.Database.Check.CheckAssignmentCompletion import CheckAssignmentCompletion
from tests.Database.DatabaseTestManager import DatabaseTestManager
import pytest

def test_SubmitAssignment():
    DatabaseTestManager.startTest()
    DeleteGradesForAssignment.update((1, 1,))
    DeleteSolutions.update((1, 1, 1,))
    SubmitAssignment.update((1, 1, 1, 1, "TEST"))
    submission = CheckAssignmentCompletion.check((1,1,1,))
    assert(submission[0][1] == "TEST")
    
    DatabaseTestManager.endTest()
    
