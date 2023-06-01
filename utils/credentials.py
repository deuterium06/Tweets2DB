import yaml
import os

from utils.constants import RDS_DB, LOCAL_DB, PROJECT_ROOT

class Credentials:
    __data = {}
    try:
        with open(os.path.join(PROJECT_ROOT, "credentials.yml")) as cred:
            __data = yaml.load(cred, Loader=yaml.SafeLoader)
    except FileNotFoundError as fnf_error:
        print(fnf_error)


    def database(self, instance=LOCAL_DB):
        if instance == RDS_DB:
            return self.__data.get(RDS_DB, {})
        elif instance == LOCAL_DB:
            return self.__data.get(LOCAL_DB, {})
        else:
            return {}