import os

# Environment Constants
DEPLOY_ENV = 'DEPLOY'
CI_ENV = 'CI'
LOCAL_ENV = 'LOCAL'

# Local DB 
LOCAL_DB = 'LOCAL'
RDS_DB = 'RDS'

# Project Directory 
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
