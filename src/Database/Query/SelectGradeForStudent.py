from src.Database.Query.DatabaseQueryAll import DatabaseQueryAll;
from src.Database.DatabaseManager import DatabaseManager;
import mysql


class SelectGradeForStudent(DatabaseQueryAll):
    @classmethod
    def queryAll(cls, dataTuple) -> tuple:
        getGrades = "SELECT Assignment.assignmentId, Grades.questionId, questionText, name, grade, comment FROM Assignment JOIN Grades ON Assignment.assignmentId = Grades.assignmentId WHERE studentId = %s AND Grades.courseId = %s"

        studentId, courseId = dataTuple
        
        cursor = DatabaseManager.getDatabaseCursor();
        cursor.execute(getGrades, (studentId, courseId))
        allGrades = cursor.fetchall();
        DatabaseManager.closeConnection();
        
        return allGrades