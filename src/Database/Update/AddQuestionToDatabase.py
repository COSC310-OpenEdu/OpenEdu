from src.Database.Update.DatabaseUpdate import DatabaseUpdate
from src.Database.DatabaseManager import DatabaseManager
import mysql

class AddQuestionoDatabase(DatabaseUpdate):
    @classmethod 
    def update(cls, dataTuple):
        question, answer, questionNum, courseId, assignmentId = dataTuple
        statement = "INSERT INTO Question(questionId, assignmentId, courseId, questionText, questionAnswer) VALUES (%s, %s, %s, %s, %s)"

        queryData = (questionNum, assignmentId, courseId, question, answer)

        cursor = DatabaseManager.getDatabaseCursor();
        cursor.execute(statement, queryData)
        

        DatabaseManager.commit()