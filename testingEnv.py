
import getpass
import json
from pprint import pprint

with open("/home/" + getpass.getuser() + "/.irods/irods_environment.json",'r') as f:
        data = json.load(f)

port = data["irods_port"]
print port
host = data["irods_host"]
print host
zone = data["irods_zone_name"]
print zone
username = data["irods_user_name"]
print username
