from src.Database.Update.AddQuestionToDatabase import AddQuestionToDatabase
from src.Database.Check.CheckAddQuestion import CheckAddQuestion
from tests.Database.DatabaseTestManager import DatabaseTestManager
import pytest

def test_AddQuestonToDatabase_single():
    DatabaseTestManager.startTest()

    AddQuestionToDatabase.update(("question","Answer",100,1,1));
    assert(CheckAddQuestion.check((100,1,1)))

    DatabaseTestManager.endTest()
    
def test_AddQuestonToDatabase_multiple():
    DatabaseTestManager.startTest()
    
    AddQuestionToDatabase.update(("question1","Answer1",101,1,1));
    AddQuestionToDatabase.update(("question2","Answer2",102,1,1));
    
    assert(CheckAddQuestion.check((101,1,1)))
    assert(CheckAddQuestion.check((102,1,1)))
    
    DatabaseTestManager.endTest()
    