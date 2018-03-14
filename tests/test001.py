import sys
sys.path.insert(0, sys.path[0] + "\\..")

import jiracloudinpython.jirarestapi as jira

def listAllProjects(server: jira.JiraServer):
    print("\nList of all projects:")
    projects = jira.getAllProjects(server)
    for p in projects:
        print(p.name)


server = sys.argv[1]
user = sys.argv[2]
password = sys.argv[3] 
print("Server: " + server)
print("User: " + user)

js = jira.JiraServer(server, user, password)

listAllProjects(js)