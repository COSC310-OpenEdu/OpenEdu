from src.Database.DatabaseManager import DatabaseManager
from src.Database.Query.DatabaseQueryAll import DatabaseQueryAll
import mysql

class SelectCoursesTaughtByInstructor(DatabaseQueryAll):
    @classmethod
    def queryAll(cls, userId) -> list:
        cursor = DatabaseManager.getDatabaseCursor();
        statement = "SELECT Course.courseId, name, credits, session, term, day, startTime, endTime FROM Instructs LEFT JOIN Course ON Instructs.courseId = Course.courseId WHERE instructorId = %s;"
        cursor.execute(statement, (userId,))
        studentData = cursor.fetchall()
        
        DatabaseManager.closeConnection();
        return studentData
    
    def extractCourseNames(courseData):
        courseNames = []
        for i in range(0,len(courseData)):
            courseNames.append(courseData[i][1])
        return courseNames