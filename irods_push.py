import sys
#import site
from irods.exception import get_exception_by_code, NetworkException
from irods.models import Collection, User, DataObject
from irods.session import iRODSSession

sess = iRODSSession(host='localhost',port=1247,user='rods',password='testpassword',zone='tempZone')

query = sess.query(Collection).filter(Collection.name == "/tempZone/home/rods/" + sys.argv[1])
results = query.all()
if len(results) <= 0:
	print "Collection doesn't exist"
	#insert code to keep creating collections as specified by the user.
	path = sys.argv[1]
	strList = path.split('/', 1 )
	if len(strList) > 1:
		currentPath = "/tempZone/home/rods/"
		for t in range(len(strList)):
			print currentPath + strList[t]
			obj = sess.collections.create(currentPath + strList[t])
			currentPath = currentPath + strList[t] + "/"
	else:
		obj = sess.collections.create("/tempZone/home/rods/" + sys.argv[1])
else:
	print "Collection exists"


pathname = "/tempZone/home/rods/" + sys.argv[1] 
if len(sys.argv) != len(set(sys.argv)):
	raise FileExistsError("Error: Can not add duplicate files, pick one.")

for x in range(2,len(sys.argv)-2,2):
#	print "I got here"
	query = sess.query(DataObject).filter(DataObject.name == sys.argv[x+1]).filter(Collection.name == pathname)
	results = query.all()
	#doesn't exist, so create it
	if len(results) <= 0:
		obj = sess.data_objects.create("/tempZone/home/rods/" + sys.argv[1] + "/" + sys.argv[x+1])
                with open(sys.argv[x]) as fileToPlace:
                        data = fileToPlace.read()

                obj = sess.data_objects.get("/tempZone/home/rods/" + sys.argv[1] + "/" + sys.argv[x+1])

                with obj.open('w') as f:
                        f.write(data)
                        f.seek(0,0)
                obj = sess.data_objects.get("/tempZone/home/rods/" + sys.argv[1] + "/" + sys.argv[x+1])
                print "Sucessfully wrote: " + sys.argv[x+1]
	#object exists so check if overwrite is checked or not. Only make a change to the file if overwrite is checked.
	else:
		if sys.argv[-1] == "true":
			obj = sess.data_objects.get("/tempZone/home/rods/" + sys.argv[1] + "/" + sys.argv[x+1])
			data = ""
			#empty the content of the file and replace with incoming file contents.
			with obj.open('w') as f:
				f.write(data)
			#	print obj
			with open(sys.argv[x]) as fileToPlace:
				data = fileToPlace.read()
			obj = sess.data_objects.get("/tempZone/home/rods/" + sys.argv[1] + "/" + sys.argv[x+1])
			with obj.open('w') as f:
				f.write(data)
				f.seek(0,0)

			obj = sess.data_objects.get("/tempZone/home/rods/" + sys.argv[1] + "/" + sys.argv[x+1])
			print "Successfully overwrited: " + sys.argv[x+1]
			
			
			

