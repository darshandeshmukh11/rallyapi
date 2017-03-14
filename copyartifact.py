import sys
from pyral import Rally, rallyWorkset
options = [arg for arg in sys.argv[1:] if arg.startswith('--')]
args    = [arg for arg in sys.argv[1:] if arg not in options]
server = "rally1.rallydev.com"
apikey = "<Your API Key>"
workspace = "<Source workspace>"
project = "<Source Project>"
rally = Rally(server,apikey=apikey, workspace=workspace, project=project)
rally.enableLogging('mypyral.log')

# Fetch the data for source user story
response = rally.get('UserStory', fetch=True, query='FormattedID = US1234')
for rec in response:

# Switch to target workspace
rally.setWorkspace("<Target workspace Name>")
rally.setProject("<Target Project Name>")
print(rec.oid, rec.Name, rec.Attachments)
rec = { "ObjectID": rec.oid, "Name": rec.Name, "Attachments": rec.Attachments }
try:
    userstory = rally.create('UserStory', rec)
except (RallyRESTException, ex):
    sys.stderr.write('ERROR: %s \n' % details)
    sys.exit(1)
print("UserStory created, ObjectID: %s  FormattedID: %s" % (userstory.oid, userstory.FormattedID))