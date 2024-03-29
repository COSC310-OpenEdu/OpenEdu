from src.Database.Update.DatabaseUpdate import DatabaseUpdate
from src.Database.DatabaseManager import DatabaseManager
import mysql

class UpdateEmail(DatabaseUpdate):
    
    #
    #   Updates the given users email
    #   If a request already exisits do nothing
    #   Input: dataTuple = (userId, email)
    #                    = The userid and email being updated
    #
    
    @classmethod
    def update(cls, dataTuple):
        (userId, email) = dataTuple;

        cursor = DatabaseManager.getDatabaseCursor()

        sql = "UPDATE User Set email = %s WHERE userId = %s";
        cursor.execute(sql, (email, userId))
        
        DatabaseManager.commit();
        return True
        