from src.Database.Query.DatabaseQueryAll import DatabaseQueryAll;
from src.Database.DatabaseManager import DatabaseManager;
import mysql

class SelectQuestionsForCourse(DatabaseQueryAll):
    
    #
    #   Returns all questions related to a specific course
    #   Input:  dataTuple = (courseId,)
    #                     = The course being searched
    #   Output: list = [[questionId, questionText, assignmentId, questionAnswer, longQuestion]]
    #                = A list of questions
    #
    
    @classmethod
    def queryAll(cls, dataTuple) -> tuple:
       
        cursor = DatabaseManager.getDatabaseCursor()
        sql = """SELECT questionId, questionText, assignmentId, questionAnswer, longQuestion FROM Question
                 WHERE courseId = %s"""
        cursor.execute(sql, (dataTuple))
        questions = cursor.fetchall()
        DatabaseManager.closeConnection()
        

        return questions