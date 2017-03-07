import sys
from pyral import Rally, rallyWorkset
options = [arg for arg in sys.argv[1:] if arg.startswith('--')]
args    = [arg for arg in sys.argv[1:] if arg not in options]
server = "rally1.rallydev.com"
apikey = "<your rally api key>"
workspace = "<rally workspace name>"
#project = "ARCHIVE-DONOTUSE"
rally = Rally(server,apikey=apikey, workspace=workspace)
rally.enableLogging('mypyral.log')
'''
workspaces = rally.getWorkspaces()
for wksp in workspaces:
    print ("%s %s" % (wksp.oid, wksp.Name))
    projects = rally.getProjects(workspace=wksp.Name)
    for proj in projects:
        print ("    %12.12s  %s  %s" % (proj.oid, proj.Name, proj.State))
'''
target_project = rally.getProject('<target project name>')
# Getting the list of projects
projects = rally.getProjects(workspace=workspace)
for proj in projects:
	children = proj.Children
	for child in children:
		if child.State == 'Closed':
			#Then update Parent to new one:
			project_fields = {
            	"ObjectID": child.oid,
            	"Parent": target_project.ref
			}
			try:
				#print("%s" % (child.Name))
				#print("    %12.12s  %s  %s" % (child.oid, child.Name, child.State))
				#print(target_project.ref)
				result = rally.update('Project', project_fields)
				print ("Project %s has been successfully updated with new %s parent" % (str(child.Name), str(child.Parent)))
			except (RallyRESTException, ex):
				print ("Update failure for Project %s" % (str(child.Name)))
				print (ex)
			#print (child.Name,child.oid,child.State,child.Description,child.Parent.__dict__)
			#exit()
	#print (children)
	#print ("    %12.12s  %s  %s" % (proj.oid, proj.Name, proj.State))