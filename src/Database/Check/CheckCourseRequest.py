from src.Database.Check.DatabaseCheck import DatabaseCheck
from src.Database.DatabaseManager import DatabaseManager
import pytest

class CheckCourseRequest(DatabaseCheck):
    
    #
    #   Returns the number of course requests for a given student and course
    #   Input:  dataTuple = (studentId, courseId)
    #   Ouput:  number of courses
    #
    
    @classmethod 
    def check(cls, dataTuple) -> bool:
        cursor = DatabaseManager.getDatabaseCursor()
        sql = "SELECT COUNT(studentId) FROM CourseRequests WHERE studentId = %s and courseId = %s"
        cursor.execute(sql, dataTuple)
        
        return cursor.fetchone()[0] == 1;
        