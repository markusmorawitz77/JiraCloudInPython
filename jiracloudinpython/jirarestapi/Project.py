from .JiraServer import JiraServer

class ProjectCategory:
    def __init__(self, json):
        self.id = json["id"]
        self.name = json["name"]
        self.description = json["description"]

class ProjectLead:
    def __init__(self, json):
        self.name = json["name"]
        self.displayName = json["displayName"]
        self.key = json["key"]
        self.accountID = json["accountId"]

class Project:
    def __init__(self, json):
        self.id = json["id"]
        self.key = json["key"]
        self.name = json["name"]
        self.lead = ProjectLead(json["lead"])
        self.description = json["description"]
        try:
            self.url = json["url"]
        except:
            self.url = ""
        self.projectCategory = ProjectCategory(json["projectCategory"])


def getAllProjects(server: JiraServer):
    r = server.getRequest("project?expand=lead,url,description")
    projects = []
    for p in r.json():
        try: 
            project = Project(p)
        except:
            continue
        projects.append(project)
    return projects



