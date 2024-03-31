from src.Database.DatabaseManager import DatabaseManager
from src.Database.Query.DatabaseQueryAll import DatabaseQueryAll
import mysql

class SelectSolutionsForCourse(DatabaseQueryAll):
    @classmethod
    def queryAll(cls, dataTuple) -> tuple:

        #
        # Retrieves every student's solution information for a course
        # Input: dataTuple = (courseId)
        # Output: A list of solution information as well as the first and last name of the students
        #

        cursor = DatabaseManager.getDatabaseCursor()
        sql = "SELECT questionId, assignmentId, studentId, firstName, lastName FROM Solution JOIN User ON User.userId = Solution.studentId WHERE courseId=%s"
        cursor.execute(sql, (dataTuple))
        people = cursor.fetchall()
        DatabaseManager.closeConnection()
        

        return people