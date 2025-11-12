# MCTHelper

As a global support representative for Microsoft Certified Trainers (MCTs), we provide MCTs with quick and accurate information on course details, summary information, lecture preparation, maintaining and renewing course qualifications, and especially, learning the latest technologies.

## Features

MCTHelper provides five core modules to support Microsoft Certified Trainers:

### 1. Course Details Management
- Add and manage course information
- Search courses by keywords
- Retrieve detailed course information including topics, duration, and level

### 2. Summary Information System
- Manage course summaries and overviews
- Access key learning points
- View prerequisites and target audience information

### 3. Lecture Preparation Tools
- Store and access preparation materials (slides, labs, demos)
- Generate preparation checklists
- Access timing guidelines for course modules

### 4. Qualification Maintenance
- Track trainer qualifications and certifications
- Monitor expiration dates with automated alerts
- Access renewal requirements and guidelines

### 5. Latest Technologies Learning
- Stay updated with latest technology versions
- Access learning paths and resources
- Browse technologies by category

## Installation

```bash
# Clone the repository
git clone https://github.com/hahaysh/MCTHelper.git
cd MCTHelper

# Install dependencies
pip install -r requirements.txt

# Install the package
pip install -e .
```

## Usage

### Command Line Interface

MCTHelper provides a convenient CLI for quick access to all features:

```bash
# List all available courses
python -m mcthelper.cli list-courses

# Show course details
python -m mcthelper.cli course-details AZ-900

# Show course summary
python -m mcthelper.cli summary AZ-900

# Show preparation checklist
python -m mcthelper.cli prep-checklist AZ-900

# Show latest technologies
python -m mcthelper.cli latest-tech
```

### Python API

You can also use MCTHelper modules directly in Python.

**Quick Example:**

```python
from mcthelper import (
    CourseDetails,
    SummaryInfo,
    LecturePreparation,
    QualificationManager,
    TechLearning
)

# Create course details manager
cd = CourseDetails()

# Add a course
cd.add_course('AZ-900', {
    'name': 'Microsoft Azure Fundamentals',
    'description': 'Introduction to cloud services and Azure',
    'duration': 1,
    'level': 'Beginner',
    'topics': ['Cloud Concepts', 'Azure Services', 'Security', 'Pricing']
})

# Search for courses
results = cd.search_courses('Azure')

# Manage qualifications
qm = QualificationManager()
qm.add_qualification('TRAINER-001', 'AZ-900', {
    'certification_date': '2024-01-01',
    'expiry_date': '2025-01-01',
    'status': 'active'
})

# Check expiration status
status = qm.check_expiry('TRAINER-001', 'AZ-900')
```

For a complete working example demonstrating all features, see [examples/usage_example.py](examples/usage_example.py).

You can run it with:
```bash
python examples/usage_example.py
```

## Running Tests

```bash
# Install test dependencies
pip install -r requirements.txt

# Run all tests
pytest

# Run tests with coverage
pytest --cov=mcthelper --cov-report=html
```

## Project Structure

```
MCTHelper/
├── mcthelper/                  # Main package
│   ├── __init__.py            # Package initialization
│   ├── cli.py                 # Command-line interface
│   └── modules/               # Core modules
│       ├── course_details.py  # Course management
│       ├── summary_info.py    # Summary information
│       ├── lecture_prep.py    # Lecture preparation
│       ├── qualifications.py  # Qualification tracking
│       └── tech_learning.py   # Technology learning
├── tests/                      # Test suite
│   ├── test_course_details.py
│   ├── test_summary_info.py
│   ├── test_lecture_prep.py
│   ├── test_qualifications.py
│   └── test_tech_learning.py
├── examples/                   # Usage examples
│   └── usage_example.py       # Complete example script
├── requirements.txt            # Dependencies
├── setup.py                    # Package setup
└── README.md                   # This file
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License.

## Support

For support, please contact the MCT support team or open an issue in the GitHub repository.
