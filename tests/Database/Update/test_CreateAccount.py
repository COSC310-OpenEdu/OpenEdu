from src.Database.Update.CreateAccount import CreateAccount
from tests.Database.DatabaseTestManager import DatabaseTestManager
from src.Database.Query.GetPrimaryKeyOfLastInsert import GetPrimaryKeyOfLastInsert
from src.Database.Check.CheckUser import CheckUser
from src.Database.Check.CheckStudent import CheckStudent
from src.Database.Check.CheckInstructor import CheckInstuctor
import pytest

def test_CreateAccount_student():
    DatabaseTestManager.startTest()
    
    CreateAccount.update(('student', 'fname', 'lname', 'email', 'password', 'username'))
    
    primaryKey = GetPrimaryKeyOfLastInsert.query(None)

    assert(CheckUser.check((primaryKey[0],)))
    assert(CheckStudent.check((primaryKey[0],)))
    
    DatabaseTestManager.endTest()

    
    
def test_CreateAccount_Instructor():
    DatabaseTestManager.startTest()
    
    CreateAccount.update(('instructor', 'fname', 'lname', 'email', 'password', 'username'))
    
    primaryKey = GetPrimaryKeyOfLastInsert.query(None)

    assert(CheckUser.check((primaryKey[0],)))
    assert(CheckInstuctor.check((primaryKey[0],)))
    
    DatabaseTestManager.endTest()

    