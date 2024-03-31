from src.Database.Update.createCourse import CreateCourse
from src.Database.Check.CheckCourse import CheckCourse
from tests.Database.DatabaseTestManager import DatabaseTestManager
import pytest


def test_CreateCourse():
    DatabaseTestManager.startTest()
    
    CreateCourse.update(('testName','testDesc',3,3,3), 3)
    assert(CheckCourse.check(('testName','testDesc',3,3,3)))
    
    DatabaseTestManager.endTest()