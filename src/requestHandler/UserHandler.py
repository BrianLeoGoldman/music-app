import json
import tornado.web

class UserHandler(tornado.web.RequestHandler):

    # get
    def get(self, userName):
        statusCode = 200
        statusMessage = 'User Obtained'
        try:
            statusMessage = self.application.db.getUser(userName)
        except Exception as e:
            raise e
            statusCode = 400
            statusMessage = 'Bad request'
        self.set_status(statusCode)
        self.write(statusMessage)

    # update data
    def put(self, userName):

        statusCode = 200
        statusMessage = 'User Updated'
        try:
            data = json.loads(self.request.body.decode('utf-8'))
            if {'name', 'lastName', 'userName'}.intersection(data.keys()) == {}:
                raise("Bad Request")
            self.application.db.updateUserData(userName, data)
        except Exception as e:
            raise e
            statusCode = 400
            statusMessage = "User was not updated"
        self.set_status(statusCode)
        self.write(statusMessage)

    # delete
    def delete(self, userName):
        statusCode = 200
        statusMessage = 'User deleted'
        try:
            self.application.db.deleteUser(userName)
        except Exception as e:
            raise e
            statusCode = 400
            statusMessage = "Bad request"
        self.set_status(statusCode)
        self.write(statusMessage)