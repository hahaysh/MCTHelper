# MCTHelper Quick Reference Guide

## Command-Line Interface (CLI)

### Basic Commands

```bash
# List all available courses
python -m mcthelper.cli list-courses

# Show detailed course information
python -m mcthelper.cli course-details <COURSE_ID>

# Show course summary
python -m mcthelper.cli summary <COURSE_ID>

# Show preparation checklist
python -m mcthelper.cli prep-checklist <COURSE_ID>

# Show latest technologies
python -m mcthelper.cli latest-tech
```

### Examples

```bash
# View Azure Fundamentals details
python -m mcthelper.cli course-details AZ-900

# Get preparation checklist for Azure Administrator
python -m mcthelper.cli prep-checklist AZ-104
```

## Python API

### 1. Course Details Management

```python
from mcthelper import CourseDetails

cd = CourseDetails()

# Add a course
cd.add_course('AZ-900', {
    'name': 'Microsoft Azure Fundamentals',
    'description': 'Introduction to cloud services',
    'duration': 1,
    'level': 'Beginner',
    'topics': ['Cloud Concepts', 'Azure Services']
})

# Search courses
results = cd.search_courses('Azure')

# Get course details
course = cd.get_course('AZ-900')

# List all courses
all_courses = cd.list_all_courses()
```

### 2. Summary Information

```python
from mcthelper import SummaryInfo

si = SummaryInfo()

# Add summary
si.add_summary('AZ-900', {
    'overview': 'Introduction to Azure',
    'key_points': ['Cloud concepts', 'Azure services'],
    'prerequisites': ['Basic IT knowledge'],
    'target_audience': 'IT professionals'
})

# Get summary
summary = si.get_summary('AZ-900')

# Get key points only
key_points = si.get_key_points('AZ-900')

# Get prerequisites only
prereqs = si.get_prerequisites('AZ-900')
```

### 3. Lecture Preparation

```python
from mcthelper import LecturePreparation

lp = LecturePreparation()

# Add preparation materials
lp.add_prep_material('AZ-900', {
    'slides': ['Module 1', 'Module 2'],
    'labs': ['Lab 1', 'Lab 2'],
    'demos': ['Demo 1'],
    'resources': ['Microsoft Learn'],
    'timing': {'Module 1': '2 hours'}
})

# Get all materials
materials = lp.get_prep_materials('AZ-900')

# Get preparation checklist
checklist = lp.get_checklist('AZ-900')

# Get timing guide
timing = lp.get_timing_guide('AZ-900')
```

### 4. Qualification Management

```python
from mcthelper import QualificationManager

qm = QualificationManager()

# Add qualification
qm.add_qualification('TRAINER-001', 'AZ-900', {
    'certification_date': '2024-01-01',
    'expiry_date': '2025-01-01',
    'status': 'active'
})

# Get all qualifications for a trainer
quals = qm.get_qualifications('TRAINER-001')

# Check expiry status (alerts if < 90 days)
status = qm.check_expiry('TRAINER-001', 'AZ-900')
# Returns: {'status': 'valid|expiring_soon|expired', 'days_remaining': N}

# Get renewal requirements
renewal = qm.get_renewal_requirements('AZ-900')
```

### 5. Technology Learning

```python
from mcthelper import TechLearning

tl = TechLearning()

# Add technology
tl.add_technology('azure-ai', {
    'name': 'Azure AI Services',
    'category': 'AI',
    'description': 'AI platform',
    'latest_version': '2024.1',
    'resources': ['Documentation', 'Blog']
})

# Get technology details
tech = tl.get_technology('azure-ai')

# Get technologies by category
ai_techs = tl.get_by_category('AI')

# Add learning path
tl.add_learning_path('ai-expert', {
    'title': 'Azure AI Expert Path',
    'technologies': ['azure-ai'],
    'modules': ['Intro', 'Advanced'],
    'duration': '8 weeks',
    'level': 'Advanced'
})

# Get learning path
path = tl.get_learning_path('ai-expert')

# Get latest updates
updates = tl.get_latest_updates()
```

## Common Use Cases

### Use Case 1: Check Trainer Qualifications

```python
from mcthelper import QualificationManager

qm = QualificationManager()

# Check all qualifications for a trainer
quals = qm.get_qualifications('TRAINER-001')

# Check for expiring certifications
for course_id in quals.keys():
    status = qm.check_expiry('TRAINER-001', course_id)
    if status['status'] == 'expiring_soon':
        print(f"Warning: {course_id} expires in {status['days_remaining']} days")
        renewal = qm.get_renewal_requirements(course_id)
        print(f"Requirements: {renewal['requirements']}")
```

### Use Case 2: Prepare for a Course

```python
from mcthelper import CourseDetails, SummaryInfo, LecturePreparation

# Get course overview
cd = CourseDetails()
course = cd.get_course('AZ-900')

# Review summary
si = SummaryInfo()
summary = si.get_summary('AZ-900')

# Get preparation checklist
lp = LecturePreparation()
checklist = lp.get_checklist('AZ-900')
timing = lp.get_timing_guide('AZ-900')
```

### Use Case 3: Stay Updated on Technologies

```python
from mcthelper import TechLearning

tl = TechLearning()

# Get latest technology updates
updates = tl.get_latest_updates()

# Browse by category
ai_techs = tl.get_by_category('AI')
devops_techs = tl.get_by_category('DevOps')

# Find learning paths
path = tl.get_learning_path('ai-expert')
```

## Data Structure Reference

### Course Information
```python
{
    'name': str,              # Course name
    'description': str,       # Course description
    'duration': int,          # Duration in days
    'level': str,            # Beginner/Intermediate/Advanced
    'topics': list[str]      # List of topics covered
}
```

### Summary Information
```python
{
    'overview': str,              # Brief overview
    'key_points': list[str],      # Key learning points
    'prerequisites': list[str],   # Prerequisites
    'target_audience': str        # Target audience description
}
```

### Preparation Materials
```python
{
    'slides': list[str],      # Slide deck references
    'labs': list[str],        # Lab exercises
    'demos': list[str],       # Demonstration guides
    'resources': list[str],   # Additional resources
    'timing': dict            # Module timing (e.g., {'Module 1': '2 hours'})
}
```

### Qualification Information
```python
{
    'certification_date': str,  # YYYY-MM-DD format
    'expiry_date': str,        # YYYY-MM-DD format
    'status': str              # active/expired/pending
}
```

### Technology Information
```python
{
    'name': str,                # Technology name
    'category': str,            # Category (AI/DevOps/Security/etc.)
    'description': str,         # Brief description
    'latest_version': str,      # Latest version
    'resources': list[str]      # Learning resources
}
```

### Learning Path
```python
{
    'title': str,               # Learning path title
    'technologies': list[str],  # Technology IDs covered
    'modules': list[str],       # Learning modules
    'duration': str,           # Estimated duration
    'level': str               # Beginner/Intermediate/Advanced
}
```

## Tips

- Use the CLI for quick lookups during training sessions
- Use the Python API for building custom workflows and integrations
- Check qualification expiry regularly (system alerts at 90 days)
- Update technology information as new versions are released
- Create learning paths to guide trainer development
- Keep preparation materials up to date with course changes
