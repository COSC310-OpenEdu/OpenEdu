from src.Database.Query.DatabaseQueryAll import DatabaseQueryAll;
from src.Database.DatabaseManager import DatabaseManager;
import mysql

class SelectGradesForCourse(DatabaseQueryAll):
    @classmethod
    def queryAll(cls, dataTuple) -> tuple:
       
        cursor = DatabaseManager.getDatabaseCursor()
        sql = """SELECT Grades.questionId, firstName, lastName, questionText, Grades.studentId, Grades.assignmentId, grade, comment FROM Grades
                JOIN Question ON Grades.questionId = Question.questionId AND Grades.assignmentId = Question.assignmentId
                JOIN User ON User.userId = Grades.studentId
                WHERE Grades.courseId = %s"""
        cursor.execute(sql, (dataTuple))
        grades = cursor.fetchall()
        DatabaseManager.closeConnection()
        

        return grades