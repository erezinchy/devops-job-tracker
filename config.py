# config.py

CSV_URL = "https://raw.githubusercontent.com/mluggy/techmap/main/jobs/devops.csv"
LOCAL_FILE = "my_jobs.csv"

TARGET_LOCATIONS = ['חיפה', 'הרצליה', 'נתניה', 'יקנעם עילית', 'קיסריה', 'רעננה', 'תל אביב-יפו']
MUST_CONTAIN = ['devops', 'site', 'platform', 'sre']
EXCLUDE_LEVELS = ['student', 'executive']
EXCLUDE_KEYWORDS = [] # Add keywords in title to skip
EXCLUDE_COMPANIES = []  # Add companies to skip
EXCLUDE_URL_KEYWORDS = []  # Add position IDs to exclude