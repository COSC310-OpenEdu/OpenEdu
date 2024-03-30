from src.Database.Update.UpdateGrade import UpdateGrade
from src.Database.Check.CheckGrade import CheckGrade
from tests.Database.DatabaseTestManager import DatabaseTestManager
import pytest

def test_UpdateGrade():
    DatabaseTestManager.startTest()
    
    UpdateGrade.update((90,1,1,1,1))
    assert(CheckGrade.check((90,1,1,1,1)))
    
    DatabaseTestManager.endTest()
    