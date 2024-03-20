from src.Database.DatabaseManager import DatabaseManager
from src.Database.Query.DatabaseQueryAll import DatabaseQueryAll
import mysql

class SelectPeopleInCourse(DatabaseQueryAll):
    @classmethod
    def queryAll(cls, dataTuple) -> tuple:
       
        cursor = DatabaseManager.getDatabaseCursor()
        sql = "SELECT Attend.studentId, firstName, lastName FROM Attend JOIN User ON Attend.studentId = User.userId WHERE courseId=%s"
        cursor.execute(sql, (dataTuple))
        people = cursor.fetchall()
        DatabaseManager.closeConnection()
        

        return people