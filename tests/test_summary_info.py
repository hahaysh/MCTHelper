"""
Tests for SummaryInfo module
"""

import pytest
from mcthelper.modules.summary_info import SummaryInfo


class TestSummaryInfo:
    """Test cases for SummaryInfo class."""
    
    def test_init(self):
        """Test SummaryInfo initialization."""
        si = SummaryInfo()
        assert si.summaries == {}
    
    def test_add_summary_success(self):
        """Test adding a valid summary."""
        si = SummaryInfo()
        summary_data = {
            'overview': 'Test overview',
            'key_points': ['Point 1', 'Point 2'],
            'prerequisites': ['Prereq 1'],
            'target_audience': 'Test audience'
        }
        result = si.add_summary('TEST-001', summary_data)
        assert result is True
        assert 'TEST-001' in si.summaries
    
    def test_add_summary_invalid_id(self):
        """Test adding a summary with invalid ID."""
        si = SummaryInfo()
        summary_data = {
            'overview': 'Test overview',
            'key_points': ['Point 1'],
            'prerequisites': ['Prereq 1'],
            'target_audience': 'Test audience'
        }
        result = si.add_summary('', summary_data)
        assert result is False
    
    def test_add_summary_missing_fields(self):
        """Test adding a summary with missing required fields."""
        si = SummaryInfo()
        summary_data = {
            'overview': 'Test overview',
            'key_points': ['Point 1']
        }
        result = si.add_summary('TEST-001', summary_data)
        assert result is False
    
    def test_get_summary_success(self):
        """Test retrieving an existing summary."""
        si = SummaryInfo()
        summary_data = {
            'overview': 'Test overview',
            'key_points': ['Point 1', 'Point 2'],
            'prerequisites': ['Prereq 1'],
            'target_audience': 'Test audience'
        }
        si.add_summary('TEST-001', summary_data)
        result = si.get_summary('TEST-001')
        assert result == summary_data
    
    def test_get_summary_not_found(self):
        """Test retrieving a non-existent summary."""
        si = SummaryInfo()
        result = si.get_summary('NOTFOUND')
        assert result is None
    
    def test_get_key_points_success(self):
        """Test getting key points for a course."""
        si = SummaryInfo()
        summary_data = {
            'overview': 'Test overview',
            'key_points': ['Point 1', 'Point 2'],
            'prerequisites': ['Prereq 1'],
            'target_audience': 'Test audience'
        }
        si.add_summary('TEST-001', summary_data)
        result = si.get_key_points('TEST-001')
        assert result == ['Point 1', 'Point 2']
    
    def test_get_key_points_not_found(self):
        """Test getting key points for non-existent course."""
        si = SummaryInfo()
        result = si.get_key_points('NOTFOUND')
        assert result == []
    
    def test_get_prerequisites_success(self):
        """Test getting prerequisites for a course."""
        si = SummaryInfo()
        summary_data = {
            'overview': 'Test overview',
            'key_points': ['Point 1'],
            'prerequisites': ['Prereq 1', 'Prereq 2'],
            'target_audience': 'Test audience'
        }
        si.add_summary('TEST-001', summary_data)
        result = si.get_prerequisites('TEST-001')
        assert result == ['Prereq 1', 'Prereq 2']
    
    def test_get_prerequisites_not_found(self):
        """Test getting prerequisites for non-existent course."""
        si = SummaryInfo()
        result = si.get_prerequisites('NOTFOUND')
        assert result == []
