"""
Summary Information Module

Provides MCTs with summary information about courses and training programs.
"""


class SummaryInfo:
    """Manages and provides summary information for MCTs."""
    
    def __init__(self):
        """Initialize the SummaryInfo manager."""
        self.summaries = {}
    
    def add_summary(self, course_id, summary_data):
        """
        Add a summary for a course.
        
        Args:
            course_id (str): Unique identifier for the course
            summary_data (dict): Dictionary containing summary information
                - overview: Brief overview
                - key_points: List of key learning points
                - prerequisites: List of prerequisites
                - target_audience: Description of target audience
        
        Returns:
            bool: True if summary added successfully
        """
        if not course_id or not isinstance(summary_data, dict):
            return False
        
        required_fields = ['overview', 'key_points', 'prerequisites', 'target_audience']
        if not all(field in summary_data for field in required_fields):
            return False
        
        self.summaries[course_id] = summary_data
        return True
    
    def get_summary(self, course_id):
        """
        Retrieve summary information by course ID.
        
        Args:
            course_id (str): Unique identifier for the course
        
        Returns:
            dict: Summary information or None if not found
        """
        return self.summaries.get(course_id)
    
    def get_key_points(self, course_id):
        """
        Get key learning points for a course.
        
        Args:
            course_id (str): Unique identifier for the course
        
        Returns:
            list: List of key points or empty list if not found
        """
        summary = self.summaries.get(course_id)
        return summary.get('key_points', []) if summary else []
    
    def get_prerequisites(self, course_id):
        """
        Get prerequisites for a course.
        
        Args:
            course_id (str): Unique identifier for the course
        
        Returns:
            list: List of prerequisites or empty list if not found
        """
        summary = self.summaries.get(course_id)
        return summary.get('prerequisites', []) if summary else []
