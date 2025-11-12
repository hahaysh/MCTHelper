"""
Course Details Module

Provides MCTs with quick and accurate information on course details.
"""


class CourseDetails:
    """Manages and provides course detail information for MCTs."""
    
    def __init__(self):
        """Initialize the CourseDetails manager."""
        self.courses = {}
    
    def add_course(self, course_id, course_info):
        """
        Add a course to the system.
        
        Args:
            course_id (str): Unique identifier for the course
            course_info (dict): Dictionary containing course details
                - name: Course name
                - description: Course description
                - duration: Duration in days
                - level: Beginner/Intermediate/Advanced
                - topics: List of topics covered
        
        Returns:
            bool: True if course added successfully
        """
        if not course_id or not isinstance(course_info, dict):
            return False
        
        required_fields = ['name', 'description', 'duration', 'level', 'topics']
        if not all(field in course_info for field in required_fields):
            return False
        
        self.courses[course_id] = course_info
        return True
    
    def get_course(self, course_id):
        """
        Retrieve course details by course ID.
        
        Args:
            course_id (str): Unique identifier for the course
        
        Returns:
            dict: Course information or None if not found
        """
        return self.courses.get(course_id)
    
    def search_courses(self, keyword):
        """
        Search for courses by keyword in name or description.
        
        Args:
            keyword (str): Search keyword
        
        Returns:
            list: List of matching courses with their IDs
        """
        if not keyword:
            return []
        
        keyword_lower = keyword.lower()
        results = []
        
        for course_id, info in self.courses.items():
            if (keyword_lower in info['name'].lower() or 
                keyword_lower in info['description'].lower()):
                results.append({'id': course_id, **info})
        
        return results
    
    def list_all_courses(self):
        """
        List all available courses.
        
        Returns:
            list: List of all courses with their IDs
        """
        return [{'id': cid, **info} for cid, info in self.courses.items()]
