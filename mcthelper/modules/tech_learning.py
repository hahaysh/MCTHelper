"""
Technology Learning Module

Helps MCTs stay updated with the latest technologies and learning resources.
"""


class TechLearning:
    """Manages technology learning resources and updates for MCTs."""
    
    def __init__(self):
        """Initialize the TechLearning manager."""
        self.technologies = {}
        self.learning_paths = {}
    
    def add_technology(self, tech_id, tech_info):
        """
        Add a new technology or update information.
        
        Args:
            tech_id (str): Unique identifier for the technology
            tech_info (dict): Dictionary containing technology information
                - name: Technology name
                - category: Category (Cloud/AI/DevOps/Security/etc.)
                - description: Brief description
                - latest_version: Latest version
                - resources: List of learning resources
        
        Returns:
            bool: True if technology added successfully
        """
        if not tech_id or not isinstance(tech_info, dict):
            return False
        
        required_fields = ['name', 'category', 'description', 'latest_version', 'resources']
        if not all(field in tech_info for field in required_fields):
            return False
        
        self.technologies[tech_id] = tech_info
        return True
    
    def get_technology(self, tech_id):
        """
        Retrieve technology information by ID.
        
        Args:
            tech_id (str): Unique identifier for the technology
        
        Returns:
            dict: Technology information or None if not found
        """
        return self.technologies.get(tech_id)
    
    def get_by_category(self, category):
        """
        Get all technologies in a specific category.
        
        Args:
            category (str): Technology category
        
        Returns:
            list: List of technologies in the category
        """
        results = []
        for tech_id, info in self.technologies.items():
            if info.get('category', '').lower() == category.lower():
                results.append({'id': tech_id, **info})
        return results
    
    def add_learning_path(self, path_id, path_info):
        """
        Add a learning path for technology mastery.
        
        Args:
            path_id (str): Unique identifier for the learning path
            path_info (dict): Dictionary containing path information
                - title: Learning path title
                - technologies: List of technology IDs covered
                - modules: List of learning modules
                - duration: Estimated duration
                - level: Beginner/Intermediate/Advanced
        
        Returns:
            bool: True if learning path added successfully
        """
        if not path_id or not isinstance(path_info, dict):
            return False
        
        required_fields = ['title', 'technologies', 'modules', 'duration', 'level']
        if not all(field in path_info for field in required_fields):
            return False
        
        self.learning_paths[path_id] = path_info
        return True
    
    def get_learning_path(self, path_id):
        """
        Retrieve a learning path by ID.
        
        Args:
            path_id (str): Unique identifier for the learning path
        
        Returns:
            dict: Learning path information or None if not found
        """
        return self.learning_paths.get(path_id)
    
    def get_latest_updates(self):
        """
        Get a summary of the latest technology updates.
        
        Returns:
            list: List of recent technology updates
        """
        # Return all technologies sorted by name for now
        updates = []
        for tech_id, info in self.technologies.items():
            updates.append({
                'id': tech_id,
                'name': info.get('name'),
                'version': info.get('latest_version'),
                'category': info.get('category')
            })
        return sorted(updates, key=lambda x: x['name'])
