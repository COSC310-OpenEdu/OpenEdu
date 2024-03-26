from src.Database.DatabaseManager import DatabaseManager
from src.Database.Query.DatabaseQueryAll import DatabaseQueryAll
import mysql

class SelectInstructorsForCourse(DatabaseQueryAll):
    @classmethod
    def queryAll(cls, dataTuple) -> tuple:
       
        cursor = DatabaseManager.getDatabaseCursor()
        sql = "SELECT Instructs.instructorId, firstName, lastName FROM Instructs JOIN User ON Instructs.instructorId = User.userId WHERE courseId=%s"
        cursor.execute(sql, (dataTuple))
        people = cursor.fetchall()
        DatabaseManager.closeConnection()
        

        return people