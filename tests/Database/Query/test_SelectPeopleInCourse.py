from src.Database.Query.SelectPeopleInCourse import SelectPeopleInCourse
import pytest

def test_numberOfPeopleCourse1():
    people = SelectPeopleInCourse.queryAll((1,))
    
    assert(len(people) == 2)
    
def test_numberOfAttributesPerPerson():
    people = SelectPeopleInCourse.queryAll((1,))
    
    assert(len(people[1]) == 3)
    
def test_personInformation():
    people = SelectPeopleInCourse.queryAll((1,))

    assert(people[0][0] == 1)
    assert(people[0][1] == 'James')
    assert(people[0][2] == 'Smith')
    
    assert(people[1][0] == 2)
    assert(people[1][1] == 'Bill')
    assert(people[1][2] == 'Murry')
