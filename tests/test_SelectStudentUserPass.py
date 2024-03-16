from src.Database.Query.SelectStudentUserPass import SelectStudentUserPass
import pytest

def test_SelectStudentUserPass():
    username = "jsmith"
    password = "jsmith1234"

    validLogin = SelectStudentUserPass.query((username,password))
    assert(validLogin[0] == 1)