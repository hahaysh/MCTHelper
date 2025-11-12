"""
MCTHelper - A support tool for Microsoft Certified Trainers (MCTs)

This package provides MCTs with quick and accurate information on:
- Course details
- Summary information
- Lecture preparation
- Maintaining and renewing course qualifications
- Learning the latest technologies
"""

__version__ = "1.0.0"

from .modules.course_details import CourseDetails
from .modules.summary_info import SummaryInfo
from .modules.lecture_prep import LecturePreparation
from .modules.qualifications import QualificationManager
from .modules.tech_learning import TechLearning

__all__ = [
    'CourseDetails',
    'SummaryInfo',
    'LecturePreparation',
    'QualificationManager',
    'TechLearning',
]
