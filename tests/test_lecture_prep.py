"""
Tests for LecturePreparation module
"""

import pytest
from mcthelper.modules.lecture_prep import LecturePreparation


class TestLecturePreparation:
    """Test cases for LecturePreparation class."""
    
    def test_init(self):
        """Test LecturePreparation initialization."""
        lp = LecturePreparation()
        assert lp.prep_materials == {}
    
    def test_add_prep_material_success(self):
        """Test adding valid preparation materials."""
        lp = LecturePreparation()
        materials = {
            'slides': ['Slide 1', 'Slide 2'],
            'labs': ['Lab 1'],
            'demos': ['Demo 1'],
            'resources': ['Resource 1'],
            'timing': {'Module 1': '1 hour'}
        }
        result = lp.add_prep_material('TEST-001', materials)
        assert result is True
        assert 'TEST-001' in lp.prep_materials
    
    def test_add_prep_material_invalid_id(self):
        """Test adding materials with invalid ID."""
        lp = LecturePreparation()
        materials = {
            'slides': ['Slide 1'],
            'labs': ['Lab 1'],
            'demos': ['Demo 1'],
            'resources': ['Resource 1'],
            'timing': {'Module 1': '1 hour'}
        }
        result = lp.add_prep_material('', materials)
        assert result is False
    
    def test_add_prep_material_missing_fields(self):
        """Test adding materials with missing required fields."""
        lp = LecturePreparation()
        materials = {
            'slides': ['Slide 1'],
            'labs': ['Lab 1']
        }
        result = lp.add_prep_material('TEST-001', materials)
        assert result is False
    
    def test_get_prep_materials_success(self):
        """Test retrieving preparation materials."""
        lp = LecturePreparation()
        materials = {
            'slides': ['Slide 1', 'Slide 2'],
            'labs': ['Lab 1'],
            'demos': ['Demo 1'],
            'resources': ['Resource 1'],
            'timing': {'Module 1': '1 hour'}
        }
        lp.add_prep_material('TEST-001', materials)
        result = lp.get_prep_materials('TEST-001')
        assert result == materials
    
    def test_get_prep_materials_not_found(self):
        """Test retrieving materials for non-existent course."""
        lp = LecturePreparation()
        result = lp.get_prep_materials('NOTFOUND')
        assert result is None
    
    def test_get_checklist_success(self):
        """Test generating preparation checklist."""
        lp = LecturePreparation()
        materials = {
            'slides': ['Slide 1'],
            'labs': ['Lab 1'],
            'demos': ['Demo 1'],
            'resources': ['Resource 1'],
            'timing': {'Module 1': '1 hour'}
        }
        lp.add_prep_material('TEST-001', materials)
        result = lp.get_checklist('TEST-001')
        assert isinstance(result, list)
        assert len(result) > 0
        assert 'Review all slide decks' in result
    
    def test_get_checklist_not_found(self):
        """Test getting checklist for non-existent course."""
        lp = LecturePreparation()
        result = lp.get_checklist('NOTFOUND')
        assert result == []
    
    def test_get_timing_guide_success(self):
        """Test getting timing guidelines."""
        lp = LecturePreparation()
        materials = {
            'slides': ['Slide 1'],
            'labs': ['Lab 1'],
            'demos': ['Demo 1'],
            'resources': ['Resource 1'],
            'timing': {'Module 1': '1 hour', 'Module 2': '2 hours'}
        }
        lp.add_prep_material('TEST-001', materials)
        result = lp.get_timing_guide('TEST-001')
        assert result == {'Module 1': '1 hour', 'Module 2': '2 hours'}
    
    def test_get_timing_guide_not_found(self):
        """Test getting timing guide for non-existent course."""
        lp = LecturePreparation()
        result = lp.get_timing_guide('NOTFOUND')
        assert result == {}
