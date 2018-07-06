import json
from hashlib import sha512
from src.requestHandler.BaseHandler import BaseHandler


class UserLoginHandler(BaseHandler):

    # update password
    def put(self, userName):
        statusCode = 200
        statusMessage = 'User Password Updated'
        try:
            data = json.loads(self.request.body.decode('utf-8'))
            if not 'password' in data.keys():
                raise ("Bad request")
            self.application.db.updateUserCredentials(userName, data)
        except Exception as e:
            #raise e
            statusCode = 400
            statusMessage = "User Password was not updated"
        self.set_status(statusCode)
        self.write(statusMessage)

    #Testing password get
    def get(self, userName):
        statusCode = 200
        statusMessage = 'User Login Obtained'
        try:
            statusMessage = self.application.db.getUserLogin(userName)
        except Exception as e:
            #raise e
            statusCode = 400
            statusMessage = 'Bad request'
        self.set_status(statusCode)
        self.write(statusMessage)

    def post(self,userName):
        statusCode = 200
        statusMessage = 'User logged-in'
        try:
            data = json.loads(self.request.body.decode('utf-8'))
            password = sha512(data['password'].encode('utf-8')).hexdigest()
            self.application.db.logginUser(userName, password)
        except Exception as e:
            #raise e
            statusCode = 400
            statusMessage = "User not logged-in"
        self.set_status(statusCode)
        self.write(statusMessage)