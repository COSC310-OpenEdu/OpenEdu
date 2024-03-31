from src.Database.Update.DeleteGradesForAssignment import DeleteGradesForAssignment

from src.Database.Query.SelectGradesForAssignment import SelectGradesForAssignment
from tests.Database.DatabaseTestManager import DatabaseTestManager
import pytest

def test_DeleteGradesForAssignment():
    DatabaseTestManager.startTest()
    
    DeleteGradesForAssignment.update(1, 1,)
    grades = SelectGradesForAssignment.queryAll((1, 1, 1,))
    assert(grades is None)
    
    DatabaseTestManager.endTest()
    
