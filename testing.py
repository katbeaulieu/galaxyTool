import password_obfuscation
import getpass
with open("/home/" + getpass.getuser() + "/.irods/.irodsA",'r') as f:
	first_line = f.readline().strip()

answer = password_obfuscation.decode(first_line)
print answer
