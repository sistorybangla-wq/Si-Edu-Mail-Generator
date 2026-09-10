from faker import Faker
import random

######## This script is only for educational purpose ########
######## use it on your own RISK ########
######## I'm not responsible for any loss or damage ########
######## caused to you using this script ########
######## Updated for September 2026 ########
######## Github Repo - https://git.io/JJisT/ ########

# Original CCC URLs
start_url = 'https://www.opencccapply.net/gateway/apply?cccMisCode='
clg_ids = ['941', '311', '361', '233', '851']
allColleges = ['MSJC College', 'Contra Costa College', 'City College', 'Sacramento College', 'Mt San Antonio']

# 2026 Update - Bangladesh Universities Database
bd_universities = {
    'BUET': {
        'id': 'bd_001',
        'name': 'Bangladesh University of Engineering & Technology',
        'domain': 'buet.ac.bd',
        'format': 'firstname@buet.ac.bd',  # Simple format
        'example': 'rahim@buet.ac.bd'
    },
    'KUET': {
        'id': 'bd_002',
        'name': 'Khulna University of Engineering & Technology',
        'domain': 'kuet.ac.bd',
        'format': 'firstname.rollno@kuet.ac.bd',  # Roll-based format
        'example': 'rahim.1803045@kuet.ac.bd'
    },
    'DU': {
        'id': 'bd_003',
        'name': 'Dhaka University',
        'domain': 'du.ac.bd',
        'format': 'firstname.std@du.ac.bd',  # Standard suffix
        'example': 'rahim.std@du.ac.bd'
    },
    'KU': {
        'id': 'bd_004',
        'name': 'Khulna University',
        'domain': 'ku.ac.bd',
        'format': 'firstname.sessionno@ku.ac.bd',  # Session-based
        'example': 'rahim.220101@ku.ac.bd'
    },
    'DUET': {
        'id': 'bd_005',
        'name': 'Dhaka University of Engineering & Technology',
        'domain': 'duet.ac.bd',
        'format': 'firstname.department@duet.ac.bd',  # Department-based
        'example': 'rahim.cmt@duet.ac.bd'
    },
    'SUST': {
        'id': 'bd_006',
        'name': 'Shahjalal University of Science & Technology',
        'domain': 'sust.edu',
        'format': 'firstname.stud@sust.edu',  # Student suffix
        'example': 'rahim.stud@sust.edu'
    },
    'RU': {
        'id': 'bd_007',
        'name': 'Rajshahi University',
        'domain': 'ru.ac.bd',
        'format': 'firstname.rollno@ru.ac.bd',  # Roll-based
        'example': 'rahim.1234@ru.ac.bd'
    },
    'IUT': {
        'id': 'bd_008',
        'name': 'Islamic University of Technology',
        'domain': 'iut-dhaka.edu',
        'format': 'firstname@iut-dhaka.edu',  # Simple format
        'example': 'rahim@iut-dhaka.edu'
    },
    'NSU': {
        'id': 'bd_009',
        'name': 'North South University',
        'domain': 'nsu.edu',
        'format': 'firstname.student@nsu.edu',  # Student suffix
        'example': 'rahim.student@nsu.edu'
    },
    'BRACU': {
        'id': 'bd_010',
        'name': 'BRAC University',
        'domain': 'bracu.ac.bd',
        'format': 'firstname.department@bracu.ac.bd',  # Department-based
        'example': 'rahim.cse@bracu.ac.bd'
    }
}

# 2026 Update - USA Universities Database
usa_universities = {
    'HARVARD': {
        'id': 'usa_001',
        'name': 'Harvard University',
        'domain': 'harvard.edu',
        'format': 'firstname@harvard.edu',  # Simple format
        'example': 'rahim@harvard.edu'
    },
    'STANFORD': {
        'id': 'usa_002',
        'name': 'Stanford University',
        'domain': 'stanford.edu',
        'format': 'firstname.std@stanford.edu',  # Student suffix
        'example': 'rahim.std@stanford.edu'
    },
    'MIT': {
        'id': 'usa_003',
        'name': 'Massachusetts Institute of Technology',
        'domain': 'mit.edu',
        'format': 'firstname[number]@mit.edu',  # With number
        'example': 'rahim123@mit.edu'
    },
    'BERKELEY': {
        'id': 'usa_004',
        'name': 'University of California, Berkeley',
        'domain': 'berkeley.edu',
        'format': '[initial].firstname@berkeley.edu',  # Initial-based
        'example': 'r.rahim@berkeley.edu'
    },
    'COLUMBIA': {
        'id': 'usa_005',
        'name': 'Columbia University',
        'domain': 'columbia.edu',
        'format': 'firstname.student@columbia.edu',  # Student suffix
        'example': 'rahim.student@columbia.edu'
    },
    'NYU': {
        'id': 'usa_006',
        'name': 'New York University',
        'domain': 'nyu.edu',
        'format': 'firstname_std@nyu.edu',  # Underscore with std
        'example': 'rahim_std@nyu.edu'
    },
    'UCLA': {
        'id': 'usa_007',
        'name': 'University of California, Los Angeles',
        'domain': 'ucla.edu',
        'format': 'firstname@ucla.edu',  # Simple format
        'example': 'rahim@ucla.edu'
    },
    'YALE': {
        'id': 'usa_008',
        'name': 'Yale University',
        'domain': 'yale.edu',
        'format': 'firstname.[gradyear]@yale.edu',  # With graduation year
        'example': 'rahim.26@yale.edu'
    },
    'PRINCETON': {
        'id': 'usa_009',
        'name': 'Princeton University',
        'domain': 'princeton.edu',
        'format': 'firstname.stud@princeton.edu',  # Student suffix
        'example': 'rahim.stud@princeton.edu'
    },
    'CORNELL': {
        'id': 'usa_010',
        'name': 'Cornell University',
        'domain': 'cornell.edu',
        'format': 'firstname@cornell.edu',  # Simple format
        'example': 'rahim@cornell.edu'
    }
}

# Department codes for email generation
departments_code = {
    'CSE': 'Computer Science & Engineering',
    'EEE': 'Electrical & Electronic Engineering',
    'ME': 'Mechanical Engineering',
    'CE': 'Civil Engineering',
    'BTE': 'Biomedical Technology & Engineering',
    'CMT': 'Computer & Management Technology',
    'ENG': 'English',
    'BUS': 'Business Administration',
    'LAW': 'Law',
    'MED': 'Medicine'
}

# Country codes for phone number generation
country_codes = ['855', '561', '800', '325', '330', '229']

# Faker instance for generating random data
fake = Faker('en_US')

ex = fake.name().split(' ')

firstName = ex[0]
LastName = ex[1]
studentAddress = fake.address()
randomMonth = random.randint(1, 12)
randomDay = random.randint(1, 27)
randomYear = random.randint(1996, 1999)
randomEduMonth = random.randint(1, 12)
randomEduDay = random.randint(1, 27)
eduYears = [2019, 2020, 2021, 2022, 2023, 2024]
randomEduYear = random.choice(eduYears)

# 2026 Update - Combined University Lists for bot selection
allUniversities = []

# Add Bangladesh universities
for key, value in bd_universities.items():
    allUniversities.append({
        'name': value['name'],
        'code': key,
        'domain': value['domain'],
        'format': value['format'],
        'country': 'Bangladesh'
    })

# Add USA universities
for key, value in usa_universities.items():
    allUniversities.append({
        'name': value['name'],
        'code': key,
        'domain': value['domain'],
        'format': value['format'],
        'country': 'USA'
    })

# Keep original CCC colleges list for backward compatibility
originalColleges = {
    'CCC_MSJC': {'name': 'MSJC College', 'id': '941'},
    'CCC_CONTRA': {'name': 'Contra Costa College', 'id': '311'},
    'CCC_CITY': {'name': 'City College', 'id': '361'},
    'CCC_SAC': {'name': 'Sacramento College', 'id': '233'},
    'CCC_MTSAN': {'name': 'Mt San Antonio', 'id': '851'}
}

# Debug mode flag
DEBUG = False

def print_debug(message):
    """Print debug messages if DEBUG is enabled"""
    if DEBUG:
        print(f"[DEBUG] {message}")

def get_university_by_country(country_name):
    """Get universities by country name"""
    unis = []
    for uni in allUniversities:
        if uni['country'].lower() == country_name.lower():
            unis.append(uni)
    return unis

def get_email_format(university_code):
    """Get email format for a specific university"""
    for key, value in bd_universities.items():
        if key == university_code:
            return value['format']
    
    for key, value in usa_universities.items():
        if key == university_code:
            return value['format']
    
    return None
