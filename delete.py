import gitlab
import sys



gl = gitlab.Gitlab( '' , private_token='' )

gl.auth()

namespace = input("Which namespace to clean up?")

groups = gl.groups.list()
group_found = 0
for group in groups:
    if (group.name == namespace):
        group_found = 1
if (group_found == 0):
    print ("Could not find group with name " + namespace + " ... aborting!" )
    sys.exit(1)


projects = gl.projects.list()
for project in projects:
    if (project.namespace["name"] == namespace):
        print(project.name_with_namespace)
        delete = input("Delete (y/n)?")
        if (delete == "y"):
            project.delete()
