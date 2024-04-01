from src.Database.Update.UpdatePassword import UpdatePassword
from src.Database.Query.SelectStudentQuery import SelectStudentQuery
from tests.Database.DatabaseTestManager import DatabaseTestManager
import pytest

def test_UpdatePassword():
    DatabaseTestManager.startTest()
    
    UpdatePassword.update((1,'jsmith1234','newpassword'))
    assert(SelectStudentQuery.query((1,))[5] == 'newpassword')
    
    DatabaseTestManager.endTest()
    
    
def test_UpdatePassword_incorrect():
    DatabaseTestManager.startTest()
    
    
    UpdatePassword.update((1,'incorrect','newpassword'))
    assert(SelectStudentQuery.query((1,))[5] != 'newpassword')
    
    DatabaseTestManager.endTest()