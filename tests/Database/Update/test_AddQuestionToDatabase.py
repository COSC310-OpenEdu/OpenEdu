from src.Database.Update.AddQuestionToDatabase import AddQuestionDatabase
from src.Database.Check.CheckAddQuestion import CheckAddQuestion
from tests.Database.DatabaseTestManager import DatabaseTestManager
import pytest

def test_AddQuestonToDatabase_single():
    try:
        AddQuestionDatabase.update(("question","Answer",100,1,1));
        assert(CheckAddQuestion.check((100,1,1)))
    except Exception:
        assert(False)
    finally:
        DatabaseTestManager.rollback()
    
def test_AddQuestonToDatabase_multiple():
    try:
        AddQuestionDatabase.update(("question1","Answer1",100,1,1));
        AddQuestionDatabase.update(("question2","Answer2",101,1,1));
    
        assert(CheckAddQuestion.check((100,1,1)))
        assert(CheckAddQuestion.check((101,1,1)))
    except Exception:
        assert(False)
    finally:
        DatabaseTestManager.rollback()