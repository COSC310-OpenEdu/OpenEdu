from src.Database.Query.SelectPeopleInCourse import SelectPeopleInCourse
from tests.Database.DatabaseTestManager import DatabaseTestManager
import pytest

def test_numberOfPeopleCourse1():
    DatabaseTestManager.startTest()
    
    people = SelectPeopleInCourse.queryAll((1,))
    assert(len(people) == 2)
    
    DatabaseTestManager.endTest()
    
    
def test_numberOfAttributesPerPerson():
    DatabaseTestManager.startTest()
    
    people = SelectPeopleInCourse.queryAll((1,))
    assert(len(people[1]) == 3)
    
    DatabaseTestManager.endTest()
    
    
def test_personInformation():
    DatabaseTestManager.startTest()
    
    people = SelectPeopleInCourse.queryAll((1,))

    assert(people[0][0] == 1)
    assert(people[0][1] == 'James')
    assert(people[0][2] == 'Smith')
    
    assert(people[1][0] == 2)
    assert(people[1][1] == 'Bill')
    assert(people[1][2] == 'Murry')
    
    DatabaseTestManager.endTest()
