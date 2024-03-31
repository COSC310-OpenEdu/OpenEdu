from src.Database.Update.DeleteGradesForAssignment import DeleteGradesForAssignment
from src.Database.Update.AddGrade import AddGrade
from src.Database.Check.CheckGrade import CheckGrade
from tests.Database.DatabaseTestManager import DatabaseTestManager
import pytest

def test_AddGrade():
    DatabaseTestManager.startTest()
    
    DeleteGradesForAssignment.update((1, 1,))
    AddGrade.update((1, 1, 1, 1, 3, 42))
    assert(CheckGrade.check((42, 1, 1, 1, 1,)) == True)
    
    DatabaseTestManager.endTest()
    
