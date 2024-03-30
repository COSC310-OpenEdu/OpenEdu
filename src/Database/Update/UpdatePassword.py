from src.Database.Update.DatabaseUpdate import DatabaseUpdate
from src.Database.DatabaseManager import DatabaseManager
import mysql

class UpdatePassword(DatabaseUpdate):
    
    #
    #   Updates the given users password if the password matches the current password
    #   If a request already exisits do nothing
    #   Input: dataTuple = (userId, curPassword, newPassword)
    #                    = The userId, current password, and new password
    #
    
    @classmethod
    def update(cls, dataTuple):
        (userId, curPassword, newPassword) = dataTuple;
        
        cursor = DatabaseManager.getDatabaseCursor()
        checkSQL = "SELECT COUNT(userId) FROM User WHERE userId = %s AND password = %s"
        cursor.execute(checkSQL, (userId, curPassword));
        print()
        if cursor.fetchone()[0] == 0:
            return False
        
        sql = "UPDATE User Set password = %s WHERE userId = %s";
        
        cursor.execute(sql, (newPassword, userId))
        
        DatabaseManager.commit();
        return True
        