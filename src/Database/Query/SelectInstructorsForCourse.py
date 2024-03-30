from src.Database.DatabaseManager import DatabaseManager
from src.Database.Query.DatabaseQueryAll import DatabaseQueryAll
import mysql

class SelectInstructorsForCourse(DatabaseQueryAll):
    
    # 
    #   Returns the Instructor ID, first name, and last name for a given course
    #   Input:  dataTuple = (courseId,)
    #                     = The course we are looking for an instructor for
    #   Output: people    = [instructorId, firstName, lastName]
    #
    
    @classmethod
    def queryAll(cls, dataTuple) -> tuple:
       
        cursor = DatabaseManager.getDatabaseCursor()
        sql = "SELECT Instructs.instructorId, firstName, lastName FROM Instructs JOIN User ON Instructs.instructorId = User.userId WHERE courseId=%s"
        cursor.execute(sql, (dataTuple))
        people = cursor.fetchall()
        DatabaseManager.closeConnection()
        

        return people