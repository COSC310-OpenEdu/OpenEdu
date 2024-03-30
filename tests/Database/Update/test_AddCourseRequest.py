from src.Database.Update.AddCourseRequest import AddCourseRequest
from src.Database.Check.CheckCourseRequest import CheckCourseRequest
from tests.Database.DatabaseTestManager import DatabaseTestManager
import pytest


def test_AddCourseRequest_Single():
    AddCourseRequest.update((1,3))
    
    assert(CheckCourseRequest.check((1,3)))
    
    DatabaseTestManager.rollback()
    
    
def test_AddCourseRequest_Multiple():
    AddCourseRequest.update((1,3))
    AddCourseRequest.update((2,3))
    
    assert(CheckCourseRequest.check((1,3)))
    assert(CheckCourseRequest.check((2,3)))
    
    DatabaseTestManager.rollback()
    DatabaseTestManager.rollback()