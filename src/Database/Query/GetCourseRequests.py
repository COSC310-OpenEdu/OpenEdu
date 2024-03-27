from src.Database.DatabaseManager import DatabaseManager

class CourseRequestManager:
    @staticmethod
    def get_course_requests():
        try:
            cursor = DatabaseManager.getDatabaseCursor()
            cursor.execute("""
                SELECT cr.studentId, cr.courseId, c.name, c.session, u.firstName, u.lastName
                FROM CourseRequests cr
                JOIN Course c ON cr.courseId = c.courseId
                JOIN User u ON cr.studentId = u.userId
                ORDER BY c.session, c.courseId
            """)
            requests = cursor.fetchall()
            
            session_mapping = {0: 'Fall', 1: 'Winter', 2: 'Summer'}
            grouped_requests = {}
            for request in requests:
                session_name = session_mapping.get(request[3], 'Unknown')
                if session_name not in grouped_requests:
                    grouped_requests[session_name] = []
                grouped_requests[session_name].append(request)

            return grouped_requests
        except Exception as e:
            print("Error fetching course requests:", e)
            return {}
