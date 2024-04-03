from src.Database.Query.DatabaseQueryAll import DatabaseQueryAll;
from src.Database.DatabaseManager import DatabaseManager;
import mysql

class SelectAssignmentsForCourse(DatabaseQueryAll):
    @classmethod
    def queryAll(cls, dataTuple) -> tuple:
       
        cursor = DatabaseManager.getDatabaseCursor()
        sql = """SELECT assignmentId, name, dueDate FROM Assignment
                 WHERE courseId = %s"""
        cursor.execute(sql, (dataTuple))
        assignments = cursor.fetchall()
        DatabaseManager.closeConnection()
        

        return assignments