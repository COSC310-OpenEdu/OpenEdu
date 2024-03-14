from DatabaseManager import DatabaseManager
import pytest


def test_ViewStudents():
    database = DatabaseManager()
    
    studentData = database.viewStudents()
    assert(studentData[0][0] == "Jayden") #Check there is a Student
    
    
    
def test_selectStudent():
    database = DatabaseManager()
    userId = 2
    
    studentData = database.selectStudent(userId)
    assert(studentData[1] == "Jayden")
    


def test_selectStudent_nonIntegerUserId():
    database = DatabaseManager()
    userId = "Cat"
    
    studentData = database.selectStudent(userId)
    assert(studentData == None)

def test_checkLogin():
    database = DatabaseManager()
    username = "jsmith"
    password = "jsmith1234"

    validLogin = database.checkLogin(username, password)
    assert(validLogin == True)

def test_checkLogin_wrongpass():
    database = DatabaseManager()
    username = "jsmith"
    password = "wrongpassword"

    validLogin = database.checkLogin(username, password)
    assert(validLogin == False)

def test_selectStudent_userpass():
    database = DatabaseManager()
    username = "jsmith"
    password = "jsmith1234"

    validLogin = database.selectStudentUserPass(username, password)
    assert(validLogin[0] == 2)