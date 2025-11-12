"""
Tests for TechLearning module
"""

import pytest
from mcthelper.modules.tech_learning import TechLearning


class TestTechLearning:
    """Test cases for TechLearning class."""
    
    def test_init(self):
        """Test TechLearning initialization."""
        tl = TechLearning()
        assert tl.technologies == {}
        assert tl.learning_paths == {}
    
    def test_add_technology_success(self):
        """Test adding a valid technology."""
        tl = TechLearning()
        tech_info = {
            'name': 'Azure AI',
            'category': 'AI',
            'description': 'AI services',
            'latest_version': '2024.1',
            'resources': ['Doc 1', 'Doc 2']
        }
        result = tl.add_technology('azure-ai', tech_info)
        assert result is True
        assert 'azure-ai' in tl.technologies
    
    def test_add_technology_invalid_id(self):
        """Test adding technology with invalid ID."""
        tl = TechLearning()
        tech_info = {
            'name': 'Azure AI',
            'category': 'AI',
            'description': 'AI services',
            'latest_version': '2024.1',
            'resources': ['Doc 1']
        }
        result = tl.add_technology('', tech_info)
        assert result is False
    
    def test_add_technology_missing_fields(self):
        """Test adding technology with missing required fields."""
        tl = TechLearning()
        tech_info = {
            'name': 'Azure AI',
            'category': 'AI'
        }
        result = tl.add_technology('azure-ai', tech_info)
        assert result is False
    
    def test_get_technology_success(self):
        """Test retrieving a technology."""
        tl = TechLearning()
        tech_info = {
            'name': 'Azure AI',
            'category': 'AI',
            'description': 'AI services',
            'latest_version': '2024.1',
            'resources': ['Doc 1']
        }
        tl.add_technology('azure-ai', tech_info)
        result = tl.get_technology('azure-ai')
        assert result == tech_info
    
    def test_get_technology_not_found(self):
        """Test retrieving non-existent technology."""
        tl = TechLearning()
        result = tl.get_technology('NOTFOUND')
        assert result is None
    
    def test_get_by_category(self):
        """Test getting technologies by category."""
        tl = TechLearning()
        tl.add_technology('azure-ai', {
            'name': 'Azure AI',
            'category': 'AI',
            'description': 'AI services',
            'latest_version': '2024.1',
            'resources': ['Doc 1']
        })
        tl.add_technology('azure-ml', {
            'name': 'Azure ML',
            'category': 'AI',
            'description': 'ML services',
            'latest_version': '2024.1',
            'resources': ['Doc 2']
        })
        tl.add_technology('azure-devops', {
            'name': 'Azure DevOps',
            'category': 'DevOps',
            'description': 'DevOps services',
            'latest_version': '2024.1',
            'resources': ['Doc 3']
        })
        
        ai_results = tl.get_by_category('AI')
        assert len(ai_results) == 2
        
        devops_results = tl.get_by_category('DevOps')
        assert len(devops_results) == 1
    
    def test_add_learning_path_success(self):
        """Test adding a valid learning path."""
        tl = TechLearning()
        path_info = {
            'title': 'AI Learning Path',
            'technologies': ['azure-ai', 'azure-ml'],
            'modules': ['Module 1', 'Module 2'],
            'duration': '4 weeks',
            'level': 'Intermediate'
        }
        result = tl.add_learning_path('ai-path', path_info)
        assert result is True
        assert 'ai-path' in tl.learning_paths
    
    def test_add_learning_path_invalid_id(self):
        """Test adding learning path with invalid ID."""
        tl = TechLearning()
        path_info = {
            'title': 'AI Learning Path',
            'technologies': ['azure-ai'],
            'modules': ['Module 1'],
            'duration': '4 weeks',
            'level': 'Intermediate'
        }
        result = tl.add_learning_path('', path_info)
        assert result is False
    
    def test_add_learning_path_missing_fields(self):
        """Test adding learning path with missing required fields."""
        tl = TechLearning()
        path_info = {
            'title': 'AI Learning Path',
            'technologies': ['azure-ai']
        }
        result = tl.add_learning_path('ai-path', path_info)
        assert result is False
    
    def test_get_learning_path_success(self):
        """Test retrieving a learning path."""
        tl = TechLearning()
        path_info = {
            'title': 'AI Learning Path',
            'technologies': ['azure-ai'],
            'modules': ['Module 1'],
            'duration': '4 weeks',
            'level': 'Intermediate'
        }
        tl.add_learning_path('ai-path', path_info)
        result = tl.get_learning_path('ai-path')
        assert result == path_info
    
    def test_get_learning_path_not_found(self):
        """Test retrieving non-existent learning path."""
        tl = TechLearning()
        result = tl.get_learning_path('NOTFOUND')
        assert result is None
    
    def test_get_latest_updates(self):
        """Test getting latest technology updates."""
        tl = TechLearning()
        tl.add_technology('azure-ai', {
            'name': 'Azure AI',
            'category': 'AI',
            'description': 'AI services',
            'latest_version': '2024.1',
            'resources': ['Doc 1']
        })
        tl.add_technology('azure-ml', {
            'name': 'Azure ML',
            'category': 'AI',
            'description': 'ML services',
            'latest_version': '2024.2',
            'resources': ['Doc 2']
        })
        
        updates = tl.get_latest_updates()
        assert len(updates) == 2
        assert all('name' in u and 'version' in u for u in updates)
