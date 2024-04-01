from src.Database.Update.UpdateEmail import UpdateEmail
from src.Database.Query.SelectStudentQuery import SelectStudentQuery
from tests.Database.DatabaseTestManager import DatabaseTestManager
import pytest

def test_UpdateEmail():
    DatabaseTestManager.startTest()
    
    UpdateEmail.update((1,'newtest@email.com'))
    assert(SelectStudentQuery.query((1,))[3] == 'newtest@email.com')
    
    DatabaseTestManager.endTest()
    
def test_UpdateEmailMultiupdate():
    DatabaseTestManager.startTest()
    
    UpdateEmail.update((1,'newtest@email.com'))
    assert(SelectStudentQuery.query((1,))[3] == 'newtest@email.com')
    
    UpdateEmail.update((1,'new@email.com'))
    assert(SelectStudentQuery.query((1,))[3] == 'new@email.com')
    
    DatabaseTestManager.endTest()