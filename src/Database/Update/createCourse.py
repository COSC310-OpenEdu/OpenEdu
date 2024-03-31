from src.Database.DatabaseManager import DatabaseManager

class CreateCourse:
    
    #
    #   Creates a new course and adds an instructor to it
    #   Input:  courseData = (courseName, description, credits, session, term)
    #           instructorId = The Id of the instructor instructing the class
    #   Output: N/A
    #
    
    @classmethod 
    def update(cls, courseData, instructorId):
        insertCourseSQL = "INSERT INTO Course (name, description, credits, session, term) VALUES (%s, %s, %s, %s, %s)"
        
        cursor = DatabaseManager.getDatabaseCursor()
        cursor.execute(insertCourseSQL, courseData)

        courseId = cursor.lastrowid #Get courseid from database

        #Assign professor to teach course
        cursor2 = DatabaseManager.getDatabaseCursor()
        statement2 = "INSERT INTO Instructs(instructorId, courseId) VALUES(%s, %s)"
        cursor2.execute(statement2, (instructorId, courseId))

