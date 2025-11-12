"""
Qualifications Module

Helps MCTs maintain and renew their course qualifications.
"""

from datetime import datetime, timedelta


class QualificationManager:
    """Manages MCT qualifications and renewal tracking."""
    
    def __init__(self):
        """Initialize the QualificationManager."""
        self.qualifications = {}
    
    def add_qualification(self, trainer_id, course_id, qualification_data):
        """
        Add a qualification for a trainer.
        
        Args:
            trainer_id (str): Unique identifier for the trainer
            course_id (str): Unique identifier for the course
            qualification_data (dict): Dictionary containing qualification info
                - certification_date: Date of certification (YYYY-MM-DD)
                - expiry_date: Expiration date (YYYY-MM-DD)
                - status: active/expired/pending
        
        Returns:
            bool: True if qualification added successfully
        """
        if not trainer_id or not course_id or not isinstance(qualification_data, dict):
            return False
        
        required_fields = ['certification_date', 'expiry_date', 'status']
        if not all(field in qualification_data for field in required_fields):
            return False
        
        if trainer_id not in self.qualifications:
            self.qualifications[trainer_id] = {}
        
        self.qualifications[trainer_id][course_id] = qualification_data
        return True
    
    def get_qualifications(self, trainer_id):
        """
        Get all qualifications for a trainer.
        
        Args:
            trainer_id (str): Unique identifier for the trainer
        
        Returns:
            dict: Dictionary of qualifications or empty dict if not found
        """
        return self.qualifications.get(trainer_id, {})
    
    def check_expiry(self, trainer_id, course_id):
        """
        Check if a qualification is expiring soon (within 90 days).
        
        Args:
            trainer_id (str): Unique identifier for the trainer
            course_id (str): Unique identifier for the course
        
        Returns:
            dict: Expiry information with status and days remaining
        """
        if trainer_id not in self.qualifications:
            return {'status': 'not_found', 'days_remaining': None}
        
        if course_id not in self.qualifications[trainer_id]:
            return {'status': 'not_found', 'days_remaining': None}
        
        qual = self.qualifications[trainer_id][course_id]
        try:
            expiry_date = datetime.strptime(qual['expiry_date'], '%Y-%m-%d')
            today = datetime.now()
            days_remaining = (expiry_date - today).days
            
            if days_remaining < 0:
                return {'status': 'expired', 'days_remaining': days_remaining}
            elif days_remaining <= 90:
                return {'status': 'expiring_soon', 'days_remaining': days_remaining}
            else:
                return {'status': 'valid', 'days_remaining': days_remaining}
        except (ValueError, KeyError):
            return {'status': 'error', 'days_remaining': None}
    
    def get_renewal_requirements(self, course_id):
        """
        Get renewal requirements for a course qualification.
        
        Args:
            course_id (str): Unique identifier for the course
        
        Returns:
            dict: Renewal requirements
        """
        # Standard renewal requirements for MCT certifications
        return {
            'course_id': course_id,
            'requirements': [
                'Complete latest course update training',
                'Pass renewal assessment',
                'Submit proof of teaching activity',
                'Complete continuing education credits'
            ],
            'renewal_period': '12 months',
            'notice_period': '90 days before expiry'
        }
