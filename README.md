# Galaxy Push Tool to push data items from Galaxy to Irods

Contains .py file, tool config xml file and basic tool dependendencies file. Relies on only the API python-irodsclient.
 
 How to add to Galaxy:
 
 Automated:
 1. Create a repository on a galaxy tool shed whether it be a local tool shed or a shared tool shed containing the three files. Make sure this tool shed is accessible to you Galaxy instance and that the iRODS component you need is installed on your computer.
 2. Locate the new repository you have created in your Galaxy instance and install the tools, making sure your tool_dependency_dir has been set in your galaxy.ini file. Otherwise Galaxy will not install the necessary API.
 3. If everything installed properly, and you remember where you said to put the tool in the Galaxy panel, your tool should now be available in your Galaxy instance.
 
Manual: 
TODO
