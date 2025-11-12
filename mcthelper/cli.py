"""
MCTHelper CLI - Command-line interface for Microsoft Certified Trainer Helper

This CLI provides quick access to all MCTHelper features.
"""

import argparse
import sys
from mcthelper import (
    CourseDetails,
    SummaryInfo,
    LecturePreparation,
    QualificationManager,
    TechLearning
)


class MCTHelperCLI:
    """Command-line interface for MCTHelper."""
    
    def __init__(self):
        """Initialize CLI with all modules."""
        self.course_details = CourseDetails()
        self.summary_info = SummaryInfo()
        self.lecture_prep = LecturePreparation()
        self.qual_manager = QualificationManager()
        self.tech_learning = TechLearning()
        self._load_sample_data()
    
    def _load_sample_data(self):
        """Load sample data for demonstration."""
        # Sample course
        self.course_details.add_course('AZ-900', {
            'name': 'Microsoft Azure Fundamentals',
            'description': 'Introduction to cloud services and Azure',
            'duration': 1,
            'level': 'Beginner',
            'topics': ['Cloud Concepts', 'Azure Services', 'Security', 'Pricing']
        })
        
        # Sample summary
        self.summary_info.add_summary('AZ-900', {
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
        
        # Sample prep materials
        self.lecture_prep.add_prep_material('AZ-900', {
            'slides': ['Module 1: Cloud Concepts', 'Module 2: Azure Services'],
            'labs': ['Lab 1: Create a VM', 'Lab 2: Configure Storage'],
            'demos': ['Demo 1: Azure Portal Tour', 'Demo 2: Resource Groups'],
            'resources': ['Microsoft Learn', 'Azure Documentation'],
            'timing': {'Module 1': '2 hours', 'Module 2': '3 hours'}
        })
        
        # Sample technology
        self.tech_learning.add_technology('azure-ai', {
            'name': 'Azure AI Services',
            'category': 'AI',
            'description': 'Comprehensive AI and machine learning platform',
            'latest_version': '2024.1',
            'resources': [
                'Azure AI Documentation',
                'Microsoft Learn - AI Path',
                'Azure AI Blog'
            ]
        })
    
    def list_courses(self):
        """List all available courses."""
        courses = self.course_details.list_all_courses()
        if not courses:
            print("No courses available.")
            return
        
        print("\n=== Available Courses ===")
        for course in courses:
            print(f"\nCourse ID: {course['id']}")
            print(f"Name: {course['name']}")
            print(f"Level: {course['level']}")
            print(f"Duration: {course['duration']} day(s)")
    
    def show_course_details(self, course_id):
        """Show detailed information about a course."""
        course = self.course_details.get_course(course_id)
        if not course:
            print(f"Course {course_id} not found.")
            return
        
        print(f"\n=== Course Details: {course_id} ===")
        print(f"Name: {course['name']}")
        print(f"Description: {course['description']}")
        print(f"Level: {course['level']}")
        print(f"Duration: {course['duration']} day(s)")
        print(f"Topics: {', '.join(course['topics'])}")
    
    def show_summary(self, course_id):
        """Show summary information for a course."""
        summary = self.summary_info.get_summary(course_id)
        if not summary:
            print(f"Summary for course {course_id} not found.")
            return
        
        print(f"\n=== Summary: {course_id} ===")
        print(f"Overview: {summary['overview']}")
        print(f"\nKey Points:")
        for point in summary['key_points']:
            print(f"  - {point}")
        print(f"\nPrerequisites:")
        for prereq in summary['prerequisites']:
            print(f"  - {prereq}")
        print(f"\nTarget Audience: {summary['target_audience']}")
    
    def show_prep_checklist(self, course_id):
        """Show preparation checklist for a course."""
        checklist = self.lecture_prep.get_checklist(course_id)
        if not checklist:
            print(f"No preparation materials found for course {course_id}.")
            return
        
        print(f"\n=== Preparation Checklist: {course_id} ===")
        for i, item in enumerate(checklist, 1):
            print(f"{i}. {item}")
    
    def show_latest_tech(self):
        """Show latest technology updates."""
        updates = self.tech_learning.get_latest_updates()
        if not updates:
            print("No technology information available.")
            return
        
        print("\n=== Latest Technologies ===")
        for tech in updates:
            print(f"\n{tech['name']} (v{tech['version']})")
            print(f"Category: {tech['category']}")


def main():
    """Main CLI entry point."""
    parser = argparse.ArgumentParser(
        description='MCTHelper - Support tool for Microsoft Certified Trainers',
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    
    subparsers = parser.add_subparsers(dest='command', help='Available commands')
    
    # List courses command
    subparsers.add_parser('list-courses', help='List all available courses')
    
    # Course details command
    details_parser = subparsers.add_parser('course-details', help='Show course details')
    details_parser.add_argument('course_id', help='Course ID')
    
    # Summary command
    summary_parser = subparsers.add_parser('summary', help='Show course summary')
    summary_parser.add_argument('course_id', help='Course ID')
    
    # Prep checklist command
    prep_parser = subparsers.add_parser('prep-checklist', help='Show preparation checklist')
    prep_parser.add_argument('course_id', help='Course ID')
    
    # Latest tech command
    subparsers.add_parser('latest-tech', help='Show latest technology updates')
    
    args = parser.parse_args()
    
    if not args.command:
        parser.print_help()
        return
    
    cli = MCTHelperCLI()
    
    if args.command == 'list-courses':
        cli.list_courses()
    elif args.command == 'course-details':
        cli.show_course_details(args.course_id)
    elif args.command == 'summary':
        cli.show_summary(args.course_id)
    elif args.command == 'prep-checklist':
        cli.show_prep_checklist(args.course_id)
    elif args.command == 'latest-tech':
        cli.show_latest_tech()


if __name__ == '__main__':
    main()
