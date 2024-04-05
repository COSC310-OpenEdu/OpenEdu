from src.Database.Query.SelectRequestableCourses import SelectRequestableCourses
import json

class CourseSearch():
    
    #
    # Returns a JSON formated list of the course list given a searchTerm
    #
    @classmethod
    def search(cls, tuple):
        courseData = SelectRequestableCourses.queryAll(tuple)
        
        return cls.jsonFormat(courseData)
        
    
    #
    # Formats the given sql row data as JSON
    #
    def jsonFormat(data):
        
        result = []
        for row in data:
            result.append(row)
        
        return json.dumps(result)