# config.py

CSV_URL = "https://raw.githubusercontent.com/mluggy/techmap/main/jobs/devops.csv"
LOCAL_FILE = "my_devops_jobs.csv"

TARGET_LOCATIONS = ['חיפה', 'הרצליה', 'נתניה', 'יקנעם עילית', 'קיסריה', 'רעננה', 'תל אביב-יפו']
MUST_CONTAIN = ['devops', 'site', 'platform', 'sre']

EXCLUDE_LEVELS = ['student', 'executive']
EXCLUDE_KEYWORDS = ['noc']
EXCLUDE_COMPANIES = ['solaredge']
EXCLUDE_URL_KEYWORDS = ['4413264678']