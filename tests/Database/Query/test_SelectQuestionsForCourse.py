from src.Database.Query.SelectQuestionsForCourse import SelectQuestionsForCourse
import pytest

def test_numberOfQuestionsCourse1():
    questions = SelectQuestionsForCourse.queryAll((1,))
    
    assert(len(questions) == 3)
    
def test_questionInformation():
    questions = SelectQuestionsForCourse.queryAll((1,))

    assert(questions[0][0] == 1)
    assert(questions[0][1] == 'This is a question 1')
    assert(questions[0][2] == 1)
    assert(questions[0][3] == 'This is the answer 1')
    
    assert(questions[1][0] == 2)
    assert(questions[1][1] == 'This is a question 2')
    assert(questions[1][2] == 1)
    assert(questions[1][3] == 'This is the answer 2')
    
    assert(questions[2][0] == 3)
    assert(questions[2][1] == 'This is a question 3')
    assert(questions[2][2] == 1)
    assert(questions[2][3] == 'This is the answer 3')
