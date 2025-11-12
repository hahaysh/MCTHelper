"""
Tests for CourseDetails module
"""

import pytest
from mcthelper.modules.course_details import CourseDetails


class TestCourseDetails:
    """Test cases for CourseDetails class."""
    
    def test_init(self):
        """Test CourseDetails initialization."""
        cd = CourseDetails()
        assert cd.courses == {}
    
    def test_add_course_success(self):
        """Test adding a valid course."""
        cd = CourseDetails()
        course_info = {
            'name': 'Test Course',
            'description': 'Test Description',
            'duration': 3,
            'level': 'Intermediate',
            'topics': ['Topic1', 'Topic2']
        }
        result = cd.add_course('TEST-001', course_info)
        assert result is True
        assert 'TEST-001' in cd.courses
    
    def test_add_course_invalid_id(self):
        """Test adding a course with invalid ID."""
        cd = CourseDetails()
        course_info = {
            'name': 'Test Course',
            'description': 'Test Description',
            'duration': 3,
            'level': 'Intermediate',
            'topics': ['Topic1', 'Topic2']
        }
        result = cd.add_course('', course_info)
        assert result is False
    
    def test_add_course_missing_fields(self):
        """Test adding a course with missing required fields."""
        cd = CourseDetails()
        course_info = {
            'name': 'Test Course',
            'description': 'Test Description'
        }
        result = cd.add_course('TEST-001', course_info)
        assert result is False
    
    def test_get_course_success(self):
        """Test retrieving an existing course."""
        cd = CourseDetails()
        course_info = {
            'name': 'Test Course',
            'description': 'Test Description',
            'duration': 3,
            'level': 'Intermediate',
            'topics': ['Topic1', 'Topic2']
        }
        cd.add_course('TEST-001', course_info)
        result = cd.get_course('TEST-001')
        assert result == course_info
    
    def test_get_course_not_found(self):
        """Test retrieving a non-existent course."""
        cd = CourseDetails()
        result = cd.get_course('NOTFOUND')
        assert result is None
    
    def test_search_courses(self):
        """Test searching for courses."""
        cd = CourseDetails()
        cd.add_course('AZ-900', {
            'name': 'Azure Fundamentals',
            'description': 'Introduction to Azure',
            'duration': 1,
            'level': 'Beginner',
            'topics': ['Cloud']
        })
        cd.add_course('AZ-104', {
            'name': 'Azure Administrator',
            'description': 'Advanced Azure administration',
            'duration': 4,
            'level': 'Intermediate',
            'topics': ['Admin']
        })
        
        results = cd.search_courses('Azure')
        assert len(results) == 2
        
        results = cd.search_courses('Fundamentals')
        assert len(results) == 1
        assert results[0]['id'] == 'AZ-900'
    
    def test_search_courses_empty_keyword(self):
        """Test searching with empty keyword."""
        cd = CourseDetails()
        results = cd.search_courses('')
        assert results == []
    
    def test_list_all_courses(self):
        """Test listing all courses."""
        cd = CourseDetails()
        cd.add_course('TEST-001', {
            'name': 'Test Course 1',
            'description': 'Description 1',
            'duration': 1,
            'level': 'Beginner',
            'topics': ['Topic1']
        })
        cd.add_course('TEST-002', {
            'name': 'Test Course 2',
            'description': 'Description 2',
            'duration': 2,
            'level': 'Intermediate',
            'topics': ['Topic2']
        })
        
        results = cd.list_all_courses()
        assert len(results) == 2
        assert any(c['id'] == 'TEST-001' for c in results)
        assert any(c['id'] == 'TEST-002' for c in results)
