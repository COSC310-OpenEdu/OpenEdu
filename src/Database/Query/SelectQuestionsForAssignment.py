from src.Database.Query.DatabaseQueryAll import DatabaseQueryAll;
from src.Database.DatabaseManager import DatabaseManager;
import mysql

class SelectQuestionsForAssignment(DatabaseQueryAll):
    @classmethod
    def queryAll(cls, dataTuple) -> tuple:
       
        cursor = DatabaseManager.getDatabaseCursor()
        sql = """SELECT questionId, questionText, assignmentId, questionAnswer, longQuestion FROM Question
                 WHERE courseId = %s and assignmentId=%s"""
        
        cursor.execute(sql, (dataTuple))
        questions = cursor.fetchall()
        DatabaseManager.closeConnection()
        

        return questions