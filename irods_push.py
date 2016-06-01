import sys
import irods.session import iRODSSession

sess = iRODSSession(host='localhost',port=1247,user='rods',password='testpassword',zone='tempZone')

obj = sess.data_objects.create("/tempZone/home/rods/" + sys.argv[1])

with open(sys.argv[1]_ as fileToPlace:
	data = fileToPlace.read()

obj = sess.data_objects.get("/tempZone/home/rods/" + sys.argv[1])
with obj.open('w') as f:
	f.write('data')
	f.seek(0,0)
