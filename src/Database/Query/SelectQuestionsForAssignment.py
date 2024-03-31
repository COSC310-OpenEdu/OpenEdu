from src.Database.Query.DatabaseQueryAll import DatabaseQueryAll;
from src.Database.DatabaseManager import DatabaseManager;
import mysql

class SelectQuestionsForAssignment(DatabaseQueryAll):
    
    #
    #   Retrieves question information for an assignment 
    #   Input:  dataTuple = (courseId, assignmentId)
    #   Output: A list of questions and its information
    #
    
    @classmethod
    def queryAll(cls, dataTuple) -> list:
       
        cursor = DatabaseManager.getDatabaseCursor()
        sql = """SELECT questionId, questionText, assignmentId, questionAnswer, longQuestion FROM Question
                 WHERE courseId = %s and assignmentId=%s"""
        
        cursor.execute(sql, (dataTuple))
        questions = cursor.fetchall()
        DatabaseManager.closeConnection()
        

        return questions