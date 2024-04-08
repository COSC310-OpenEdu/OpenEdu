from src.Database.Query.DatabaseQuery import DatabaseQuery
from src.Database.DatabaseManager import DatabaseManager

class GetEssayLocation(DatabaseQuery):
    
    #
    #   Returns the location of the essay in the database for the requested course, student and assignement 
    #   Input:  dataTuple = (courseId, assignmentId, studentId)
    #
    
    @classmethod
    def query(cls, dataTuple) -> tuple:
        
        cursor = DatabaseManager.getDatabaseCursor()
        
        sql = "SELECT studentAnswer FROM SOLUTION WHERE courseId = %s AND questionId = 1 AND assignmentId = %s AND studentId = %s"
        
        cursor.execute(sql, dataTuple)