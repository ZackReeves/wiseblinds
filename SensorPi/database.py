import time
from google.oauth2 import service_account
from google.auth.transport.requests import AuthorizedSession

class Database:

    def __init__(self):
        self.db = "https://wiseblinds-default-rtdb.europe-west1.firebasedatabase.app/"
        self.keyfile = #Private keyfile to access database
        self.scopes = [
            "https://www.googleapis.com/auth/userinfo.email",
            "https://www.googleapis.com/auth/firebase.database"
            ]
        self.credentials = service_account.Credentials.from_service_account_file(self.keyfile, scopes=self.scopes)
        self.authed_session = AuthorizedSession(self.credentials)

    def read(self, path, query):
        response = self.authed_session.get(self.db+path+query)

        if response.ok:
            data = response.json()
            return data
        else:
            raise ConnectionError("Could not read from database: {}".format(response.text))
         

    def write(self, type, path, data):

        if type == "put":
            response = self.authed_session.put(self.db+path, json=data)
        elif type == "post":
            response = self.authed_session.post(self.db+path, json=data)
        
        if response.ok:
            return True
        else:
            raise ConnectionError("Could not write to database: {}".format(response.text))