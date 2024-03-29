from src.Database.Query.DatabaseQueryAll import DatabaseQueryAll;
from src.Database.DatabaseManager import DatabaseManager;
import mysql

class SelectQuestionsForCourse(DatabaseQueryAll):
    @classmethod
    def queryAll(cls, dataTuple) -> tuple:
       
        cursor = DatabaseManager.getDatabaseCursor()
        sql = """SELECT questionId, questionText, assignmentId, questionAnswer, longQuestion FROM Question
                 WHERE courseId = %s"""
        cursor.execute(sql, (dataTuple))
        questions = cursor.fetchall()
        DatabaseManager.closeConnection()
        

        return questions