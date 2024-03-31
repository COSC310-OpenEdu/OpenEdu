from src.Database.DatabaseManager import DatabaseManager
from src.Database.Query.DatabaseQueryAll import DatabaseQueryAll
import mysql

class SelectPeopleInCourse(DatabaseQueryAll):
    
    #
    #   Returns the people in the given course
    #   Input:  dataTuple = (courseId,)
    #                     = The course being searched
    #   Output: people    = [[studentId, firstName, lastName]]
    #                     = A list of people in the course 
    #
    
    @classmethod
    def queryAll(cls, dataTuple) -> tuple:
       
        cursor = DatabaseManager.getDatabaseCursor()
        sql = "SELECT Attend.studentId, firstName, lastName FROM Attend JOIN User ON Attend.studentId = User.userId WHERE courseId=%s"
        cursor.execute(sql, (dataTuple))
        people = cursor.fetchall()
        DatabaseManager.closeConnection()
        

        return people