from src.Database.Query.DatabaseQueryAll import DatabaseQueryAll;
from src.Database.DatabaseManager import DatabaseManager;
import mysql

class SelectAssignmentsForCourse(DatabaseQueryAll):
    
    #
    #   Selects information for all assignment from a given course
    #   Input:  dataTuple = (courseId,)
    #   Ouput:  A list of assignments
    
    @classmethod
    def queryAll(cls, dataTuple) -> tuple:
       
        cursor = DatabaseManager.getDatabaseCursor()
        sql = """SELECT assignmentId, name, dueDate, quiz FROM Assignment
                 WHERE courseId = %s"""
        cursor.execute(sql, (dataTuple))
        assignments = cursor.fetchall()
        DatabaseManager.closeConnection()
        

        return assignments