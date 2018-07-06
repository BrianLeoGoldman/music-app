import json
from src.requestHandler.BaseHandler import BaseHandler


class TrackHandler(BaseHandler):

    def get(self,trackId):
        statusCode = 200
        statusMessage = ''
        try:
            statusMessage = self.application.db.getTrack(trackId)
        except Exception as e:
            #raise e
            statusCode = 400
            statusMessage = "Bad request"
        self.set_status(statusCode)
        self.write(statusMessage)

    def delete(self,trackId):
        statusCode = 200
        statusMessage = 'Album deleted'
        try:
            self.application.db.deleteTrack(trackId)
        except Exception as e:
            #raise e
            statusMessage = 'Track not deleted'
            statusCode = 400
        self.set_status(statusCode)
        self.write(statusMessage)

    def put(self,trackId):
        statusCode = 200
        statusMessage = 'Track updated'
        try:
            data= json.loads(self.request.body.decode('utf-8'))
            if 'owner' not in data.keys():
                raise ('Bad Request')
            owner = data['owner']
            if self.application.db.isLoggedin(owner):
                self.application.db.updateTrack(trackId,data)
            else:
                statusCode = 403
                statusMessage = 'User invalid or not loggedin'
        except Exception as e:
            #raise e
            statusMessage = 'Track not update'
            statusCode = 400
        self.set_status(statusCode)
        self.write(statusMessage)