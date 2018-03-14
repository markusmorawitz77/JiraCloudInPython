import requests

class JiraServer:
    def __init__(self, server, user, password):
        self.server = server
        self.user = user
        self.password = password
        self.restAPI = "/rest/api/2/"

    def getRequest(self, request):
        return requests.get(self.server + self.restAPI + request, 
                            auth = (self.user, self.password))
