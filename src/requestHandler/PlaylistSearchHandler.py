import json
from src.requestHandler.BaseHandler import BaseHandler

class PlaylistSearchHandler(BaseHandler):

    def get(self):
        statusCode = 200
        statusMessage = ''
        try:
            playlistLikeName = self.get_argument('playlistLikeName')
            statusMessage = self.application.db.getPlaylistLikeName(playlistLikeName)
        except Exception as e:
            #raise e
            statusCode = 400
            statusMessage = "Bad request"
        self.set_status(statusCode)
        self.write(statusMessage)

    def get(self):
        statusCode = 200
        statusMessage = ''
        try:
            statusMessage = self.application.db.getAllPlaylists()
        except Exception as e:
            #raise e
            statusCode = 400
            statusMessage = "Bad request"
        self.set_status(statusCode)
        self.write(statusMessage)

    def put(self):
        statusCode = 200
        statusMessage = 'Playlist added'
        try:
            data = json.loads(self.request.body.decode('utf-8'))
            playlistName = data['playlistName']
            userName = data['userName']
            description = data['description']
            if self.application.db.isLoggedin(userName):
                self.application.db.addPlaylist(playlistName, userName, description)
            else:
                statusCode = 403
                statusMessage = 'User invalid or not logged in'
        except Exception as e:
            #raise e
            statusCode = 400
            statusMessage = "Playlist not added"
        self.set_status(statusCode)
        self.write(statusMessage)

    def delete(self):
        statusCode = 200
        statusMessage = 'Tracks deleted from playlist'
        try:
            data = json.loads(self.request.body.decode('utf-8'))
            playlistName = data['playlistName']
            tracks = data['tracks']
            self.application.db.deleteTracksFromPlaylist(playlistName, tracks)
        except Exception as e:
            #raise e
            statusCode = 400
            statusMessage = "Tracks not deleted"
        self.set_status(statusCode)
        self.write(statusMessage)
