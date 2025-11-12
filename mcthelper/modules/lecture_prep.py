"""
Lecture Preparation Module

Helps MCTs prepare for lectures with structured guidance and resources.
"""


class LecturePreparation:
    """Manages lecture preparation materials and guidelines for MCTs."""
    
    def __init__(self):
        """Initialize the LecturePreparation manager."""
        self.prep_materials = {}
    
    def add_prep_material(self, course_id, materials):
        """
        Add preparation materials for a course.
        
        Args:
            course_id (str): Unique identifier for the course
            materials (dict): Dictionary containing preparation materials
                - slides: List of slide deck references
                - labs: List of lab exercises
                - demos: List of demonstration guides
                - resources: List of additional resources
                - timing: Suggested timing for each module
        
        Returns:
            bool: True if materials added successfully
        """
        if not course_id or not isinstance(materials, dict):
            return False
        
        required_fields = ['slides', 'labs', 'demos', 'resources', 'timing']
        if not all(field in materials for field in required_fields):
            return False
        
        self.prep_materials[course_id] = materials
        return True
    
    def get_prep_materials(self, course_id):
        """
        Retrieve preparation materials by course ID.
        
        Args:
            course_id (str): Unique identifier for the course
        
        Returns:
            dict: Preparation materials or None if not found
        """
        return self.prep_materials.get(course_id)
    
    def get_checklist(self, course_id):
        """
        Generate a preparation checklist for a course.
        
        Args:
            course_id (str): Unique identifier for the course
        
        Returns:
            list: List of preparation tasks
        """
        materials = self.prep_materials.get(course_id)
        if not materials:
            return []
        
        checklist = [
            "Review all slide decks",
            "Test all lab exercises",
            "Practice demonstrations",
            "Verify all resources are accessible",
            "Review timing for each module",
            "Prepare Q&A scenarios"
        ]
        
        return checklist
    
    def get_timing_guide(self, course_id):
        """
        Get timing guidelines for course modules.
        
        Args:
            course_id (str): Unique identifier for the course
        
        Returns:
            dict: Timing information or empty dict if not found
        """
        materials = self.prep_materials.get(course_id)
        return materials.get('timing', {}) if materials else {}
