#!/usr/bin/env python
"""
Example usage of MCTHelper modules

This script demonstrates how to use all MCTHelper features.
"""

from mcthelper import (
    CourseDetails,
    SummaryInfo,
    LecturePreparation,
    QualificationManager,
    TechLearning
)
from datetime import datetime, timedelta


def main():
    print("=" * 60)
    print("MCTHelper - Example Usage")
    print("=" * 60)
    
    # 1. Course Details Management
    print("\n1. COURSE DETAILS MANAGEMENT")
    print("-" * 60)
    
    cd = CourseDetails()
    
    # Add multiple courses
    courses = [
        ('AZ-900', {
            'name': 'Microsoft Azure Fundamentals',
            'description': 'Introduction to cloud services and Azure',
            'duration': 1,
            'level': 'Beginner',
            'topics': ['Cloud Concepts', 'Azure Services', 'Security', 'Pricing']
        }),
        ('AZ-104', {
            'name': 'Microsoft Azure Administrator',
            'description': 'Administer Azure subscriptions and resources',
            'duration': 4,
            'level': 'Intermediate',
            'topics': ['Identity', 'Governance', 'Storage', 'Compute', 'Networking']
        }),
        ('AI-102', {
            'name': 'Designing and Implementing Azure AI Solutions',
            'description': 'Build AI solutions using Azure AI services',
            'duration': 4,
            'level': 'Advanced',
            'topics': ['Azure AI', 'Machine Learning', 'Computer Vision', 'NLP']
        })
    ]
    
    for course_id, course_info in courses:
        cd.add_course(course_id, course_info)
        print(f"Added course: {course_info['name']}")
    
    # Search for courses
    print("\nSearching for 'Azure' courses:")
    results = cd.search_courses('Azure')
    for course in results:
        print(f"  - {course['id']}: {course['name']} ({course['level']})")
    
    # 2. Summary Information
    print("\n2. SUMMARY INFORMATION")
    print("-" * 60)
    
    si = SummaryInfo()
    
    si.add_summary('AZ-900', {
        'overview': 'This course provides foundational knowledge of cloud services and Azure.',
        'key_points': [
            'Understand cloud computing concepts',
            'Learn core Azure services',
            'Understand Azure security and compliance',
            'Understand Azure pricing and support'
        ],
        'prerequisites': ['Basic understanding of IT concepts'],
        'target_audience': 'IT professionals new to cloud computing'
    })
    
    summary = si.get_summary('AZ-900')
    print(f"Summary for AZ-900:")
    print(f"  Overview: {summary['overview']}")
    print(f"  Key Points: {len(summary['key_points'])} points")
    print(f"  Prerequisites: {summary['prerequisites']}")
    
    # 3. Lecture Preparation
    print("\n3. LECTURE PREPARATION")
    print("-" * 60)
    
    lp = LecturePreparation()
    
    lp.add_prep_material('AZ-900', {
        'slides': [
            'Module 1: Cloud Concepts',
            'Module 2: Azure Services',
            'Module 3: Security and Compliance',
            'Module 4: Pricing and Support'
        ],
        'labs': [
            'Lab 1: Create a Virtual Machine',
            'Lab 2: Configure Storage',
            'Lab 3: Implement Azure Security'
        ],
        'demos': [
            'Demo 1: Azure Portal Tour',
            'Demo 2: Resource Groups',
            'Demo 3: Cost Management'
        ],
        'resources': [
            'Microsoft Learn',
            'Azure Documentation',
            'Microsoft Training Videos'
        ],
        'timing': {
            'Module 1': '2 hours',
            'Module 2': '3 hours',
            'Module 3': '2 hours',
            'Module 4': '1 hour'
        }
    })
    
    checklist = lp.get_checklist('AZ-900')
    print("Preparation Checklist for AZ-900:")
    for i, item in enumerate(checklist, 1):
        print(f"  {i}. {item}")
    
    # 4. Qualification Management
    print("\n4. QUALIFICATION MANAGEMENT")
    print("-" * 60)
    
    qm = QualificationManager()
    
    # Add qualifications for trainers
    trainers = [
        ('TRAINER-001', 'AZ-900', {
            'certification_date': '2024-01-01',
            'expiry_date': (datetime.now() + timedelta(days=200)).strftime('%Y-%m-%d'),
            'status': 'active'
        }),
        ('TRAINER-001', 'AZ-104', {
            'certification_date': '2024-06-01',
            'expiry_date': (datetime.now() + timedelta(days=60)).strftime('%Y-%m-%d'),
            'status': 'active'
        }),
        ('TRAINER-002', 'AI-102', {
            'certification_date': '2023-01-01',
            'expiry_date': (datetime.now() - timedelta(days=30)).strftime('%Y-%m-%d'),
            'status': 'expired'
        })
    ]
    
    for trainer_id, course_id, qual_data in trainers:
        qm.add_qualification(trainer_id, course_id, qual_data)
    
    print("Checking qualification status for TRAINER-001:")
    for course_id in ['AZ-900', 'AZ-104']:
        status = qm.check_expiry('TRAINER-001', course_id)
        print(f"  {course_id}: {status['status']} ({status['days_remaining']} days remaining)")
    
    # Show renewal requirements
    print("\nRenewal requirements for AZ-900:")
    renewal = qm.get_renewal_requirements('AZ-900')
    for req in renewal['requirements']:
        print(f"  - {req}")
    
    # 5. Technology Learning
    print("\n5. TECHNOLOGY LEARNING")
    print("-" * 60)
    
    tl = TechLearning()
    
    # Add technologies
    technologies = [
        ('azure-ai', {
            'name': 'Azure AI Services',
            'category': 'AI',
            'description': 'Comprehensive AI and machine learning platform',
            'latest_version': '2024.1',
            'resources': [
                'Azure AI Documentation',
                'Microsoft Learn - AI Path',
                'Azure AI Blog'
            ]
        }),
        ('azure-devops', {
            'name': 'Azure DevOps',
            'category': 'DevOps',
            'description': 'Complete DevOps toolchain for application development',
            'latest_version': '2024.2',
            'resources': [
                'Azure DevOps Documentation',
                'Microsoft Learn - DevOps Path',
                'Azure DevOps Blog'
            ]
        }),
        ('azure-security', {
            'name': 'Azure Security Center',
            'category': 'Security',
            'description': 'Unified security management and threat protection',
            'latest_version': '2024.1',
            'resources': [
                'Azure Security Documentation',
                'Microsoft Security Blog',
                'Security Best Practices'
            ]
        })
    ]
    
    for tech_id, tech_info in technologies:
        tl.add_technology(tech_id, tech_info)
        print(f"Added technology: {tech_info['name']} v{tech_info['latest_version']}")
    
    # Add learning path
    tl.add_learning_path('ai-expert', {
        'title': 'Azure AI Expert Path',
        'technologies': ['azure-ai'],
        'modules': [
            'Introduction to Azure AI',
            'Computer Vision',
            'Natural Language Processing',
            'Machine Learning',
            'Advanced AI Solutions'
        ],
        'duration': '8 weeks',
        'level': 'Advanced'
    })
    
    print("\nLearning Path: Azure AI Expert")
    path = tl.get_learning_path('ai-expert')
    print(f"  Duration: {path['duration']}")
    print(f"  Level: {path['level']}")
    print(f"  Modules: {len(path['modules'])}")
    
    # Get technologies by category
    print("\nAI Category Technologies:")
    ai_techs = tl.get_by_category('AI')
    for tech in ai_techs:
        print(f"  - {tech['name']} v{tech['latest_version']}")
    
    print("\n" + "=" * 60)
    print("Example completed successfully!")
    print("=" * 60)


if __name__ == '__main__':
    main()
