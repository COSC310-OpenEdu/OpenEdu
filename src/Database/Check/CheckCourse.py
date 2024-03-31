from src.Database.Check.DatabaseCheck import DatabaseCheck
from src.Database.DatabaseManager import DatabaseManager
import pytest

class CheckCourse(DatabaseCheck):
    
    #
    #   Checks  where there exists a course with the inputted information
    #   Input:  dataTuple = (courseName, description, credits, session, term)
    #   Ouput:  True if the course exists
    #           False if the course does not exist
    #

    @classmethod
    def check(cls, dataTuple) -> bool:
        cursor = DatabaseManager.getDatabaseCursor()
        sql = "SELECT COUNT(courseId) FROM Course WHERE name = %s AND description = %s AND credits = %s AND session = %s AND term = %s"
        cursor.execute(sql, dataTuple)
        
        return cursor.fetchone()[0] > 0