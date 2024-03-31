from src.Database.Update.AddCourseRequest import AddCourseRequest
from src.Database.Check.CheckCourseRequest import CheckCourseRequest
from tests.Database.DatabaseTestManager import DatabaseTestManager
import pytest


def test_AddCourseRequest_Single():
    DatabaseTestManager.startTest()
    
    AddCourseRequest.update((1,3))
    
    assert(CheckCourseRequest.check((1,3)))
    
    DatabaseTestManager.endTest()
    
    
def test_AddCourseRequest_Multiple():
    DatabaseTestManager.startTest()
    
    AddCourseRequest.update((1,3))
    AddCourseRequest.update((2,3))
    
    assert(CheckCourseRequest.check((1,3)))
    assert(CheckCourseRequest.check((2,3)))
    
    DatabaseTestManager.endTest()