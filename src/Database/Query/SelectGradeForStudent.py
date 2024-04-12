from src.Database.Query.DatabaseQueryAll import DatabaseQueryAll;
from src.Database.DatabaseManager import DatabaseManager;
import mysql


class SelectGradeForStudent(DatabaseQueryAll):
    
    #
    #   Gets all the grades for a given student in a given course
    #   Input:  dataTuple = (studentId, courseId)
    #   Output: A list of grade information
    #
    
    @classmethod
    def queryAll(cls, dataTuple) -> tuple:
        getGrades = "SELECT Assignment.assignmentId, Grades.questionId, questionText, name, grade, comment FROM Assignment JOIN Grades ON Assignment.assignmentId = Grades.assignmentId JOIN Question ON Question.questionId = Grades.questionId and Question.assignmentId = Grades.assignmentId WHERE Grades.studentId = %s AND Grades.courseId = %s"
 
        cursor = DatabaseManager.getDatabaseCursor();
        cursor.execute(getGrades, (dataTuple))
        allGrades = cursor.fetchall();
        DatabaseManager.closeConnection();
        
        return allGrades