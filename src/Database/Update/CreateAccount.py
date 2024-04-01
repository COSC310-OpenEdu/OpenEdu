from src.Database.Update.DatabaseUpdate import DatabaseUpdate
from src.Database.DatabaseManager import DatabaseManager
import mysql

class CreateAccount(DatabaseUpdate):
    
    #
    #   Creates a user and assigns them as an instructor depending on input
    #   Input:  dataTuple = (accountType, firstName, lastName, email, password, username)
    #                     = accountType options ['student', 'teacher'] 
    #   Output: N/A
    #
    
    @classmethod 
    def update(cls, dataTuple):
        
        
        createUser = ("INSERT INTO User (firstName, lastName, email, password, username) VALUES (%s, %s, %s, %s, %s);");
        createTeacher = ("INSERT INTO Instructor (userId) VALUES (LAST_INSERT_ID());");
        createStudent = ("INSERT INTO Student (userId) VALUES (LAST_INSERT_ID());");
        
        accountType, fname, lname, email, password, uname = dataTuple
        
        cursor = DatabaseManager.getDatabaseCursor();
        
        userData = (fname, lname, email, password, uname);
        cursor.execute(createUser, userData);
        
        # Create a student or instructor account depending on user's choice 
        if (accountType == 'student'):
            cursor.execute(createStudent);
        else:
            cursor.execute(createTeacher);