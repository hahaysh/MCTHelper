"""
Tests for QualificationManager module
"""

import pytest
from datetime import datetime, timedelta
from mcthelper.modules.qualifications import QualificationManager


class TestQualificationManager:
    """Test cases for QualificationManager class."""
    
    def test_init(self):
        """Test QualificationManager initialization."""
        qm = QualificationManager()
        assert qm.qualifications == {}
    
    def test_add_qualification_success(self):
        """Test adding a valid qualification."""
        qm = QualificationManager()
        qual_data = {
            'certification_date': '2024-01-01',
            'expiry_date': '2025-01-01',
            'status': 'active'
        }
        result = qm.add_qualification('TRAINER-001', 'TEST-001', qual_data)
        assert result is True
        assert 'TRAINER-001' in qm.qualifications
        assert 'TEST-001' in qm.qualifications['TRAINER-001']
    
    def test_add_qualification_invalid_trainer_id(self):
        """Test adding qualification with invalid trainer ID."""
        qm = QualificationManager()
        qual_data = {
            'certification_date': '2024-01-01',
            'expiry_date': '2025-01-01',
            'status': 'active'
        }
        result = qm.add_qualification('', 'TEST-001', qual_data)
        assert result is False
    
    def test_add_qualification_missing_fields(self):
        """Test adding qualification with missing required fields."""
        qm = QualificationManager()
        qual_data = {
            'certification_date': '2024-01-01'
        }
        result = qm.add_qualification('TRAINER-001', 'TEST-001', qual_data)
        assert result is False
    
    def test_get_qualifications_success(self):
        """Test retrieving qualifications for a trainer."""
        qm = QualificationManager()
        qual_data = {
            'certification_date': '2024-01-01',
            'expiry_date': '2025-01-01',
            'status': 'active'
        }
        qm.add_qualification('TRAINER-001', 'TEST-001', qual_data)
        result = qm.get_qualifications('TRAINER-001')
        assert 'TEST-001' in result
        assert result['TEST-001'] == qual_data
    
    def test_get_qualifications_not_found(self):
        """Test retrieving qualifications for non-existent trainer."""
        qm = QualificationManager()
        result = qm.get_qualifications('NOTFOUND')
        assert result == {}
    
    def test_check_expiry_valid(self):
        """Test checking expiry for valid qualification."""
        qm = QualificationManager()
        future_date = (datetime.now() + timedelta(days=180)).strftime('%Y-%m-%d')
        qual_data = {
            'certification_date': '2024-01-01',
            'expiry_date': future_date,
            'status': 'active'
        }
        qm.add_qualification('TRAINER-001', 'TEST-001', qual_data)
        result = qm.check_expiry('TRAINER-001', 'TEST-001')
        assert result['status'] == 'valid'
        assert result['days_remaining'] > 90
    
    def test_check_expiry_expiring_soon(self):
        """Test checking expiry for soon-to-expire qualification."""
        qm = QualificationManager()
        soon_date = (datetime.now() + timedelta(days=60)).strftime('%Y-%m-%d')
        qual_data = {
            'certification_date': '2024-01-01',
            'expiry_date': soon_date,
            'status': 'active'
        }
        qm.add_qualification('TRAINER-001', 'TEST-001', qual_data)
        result = qm.check_expiry('TRAINER-001', 'TEST-001')
        assert result['status'] == 'expiring_soon'
        assert result['days_remaining'] <= 90
    
    def test_check_expiry_expired(self):
        """Test checking expiry for expired qualification."""
        qm = QualificationManager()
        past_date = (datetime.now() - timedelta(days=30)).strftime('%Y-%m-%d')
        qual_data = {
            'certification_date': '2023-01-01',
            'expiry_date': past_date,
            'status': 'expired'
        }
        qm.add_qualification('TRAINER-001', 'TEST-001', qual_data)
        result = qm.check_expiry('TRAINER-001', 'TEST-001')
        assert result['status'] == 'expired'
        assert result['days_remaining'] < 0
    
    def test_check_expiry_not_found(self):
        """Test checking expiry for non-existent qualification."""
        qm = QualificationManager()
        result = qm.check_expiry('NOTFOUND', 'TEST-001')
        assert result['status'] == 'not_found'
        assert result['days_remaining'] is None
    
    def test_get_renewal_requirements(self):
        """Test getting renewal requirements."""
        qm = QualificationManager()
        result = qm.get_renewal_requirements('TEST-001')
        assert 'course_id' in result
        assert 'requirements' in result
        assert isinstance(result['requirements'], list)
        assert len(result['requirements']) > 0
