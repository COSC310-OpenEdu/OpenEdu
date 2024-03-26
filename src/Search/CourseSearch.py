from src.Database.Query.SelectCourseQueryAll import SelectCourseQueryAll
import json

class CourseSearch():
    
    @classmethod
    def search(cls, searchTerm):
        courseData = SelectCourseQueryAll.queryAll((searchTerm,))
        
        return cls.jsonFormat(courseData)
        
    
    def jsonFormat(data):
        
        result = []
        for row in data:
            result.append(row)
        
        return json.dumps(result)