from src.Database.Query.DatabaseQueryAll import DatabaseQueryAll;
from src.Database.DatabaseManager import DatabaseManager;
import mysql

class SelectAllInstructors(DatabaseQueryAll):
    @classmethod
    def queryAll(cls) -> list:
        cursor = DatabaseManager.getDatabaseCursor()

        statement = "SELECT Instructor.userId, User.firstName, User.lastName FROM Instructor LEFT JOIN User ON Instructor.userId = User.userId" 

        cursor.execute(statement)

        instructorData = cursor.fetchall()

        instructorId = [row[0] for row in instructorData]
        instructorName = [row[1] +" "+ row[2] for row in instructorData]
        return instructorId, instructorName


