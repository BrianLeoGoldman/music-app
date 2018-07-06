import json
import unittest
from collections import namedtuple
from src.appConfig import ENV
from src.TestService import *
import requests

class TrackTestCase(unittest.TestCase):

    def getFilePath(self,fileName):
        return 'rsc/'+fileName if ENV == 'dev' else 'test/rsc/'+fileName

    def test_addTrack_Tema1_by_JoseYYY_When_is_logged(self):
        createJosePerez()
        logJosePerez()

        fileFullPath = self.getFilePath('metallica_fuell.mp3')
        files= {'file': open(fileFullPath, 'rb')}
        putData = {'trackName': 'Tema 1', 'owner': 'JoseYYY'}
        addTrackReq = requests.post('http://localhost:8080/apiv1/tracks', files=files,data=putData)

        self.assertEqual(200,addTrackReq .status_code)
        self.assertEqual('OK',addTrackReq .reason)
        self.assertEqual('Track added',addTrackReq .text)
        logoutJosePerez()

    @unittest.skip
    def test_addTrack_Tema1_by_JoseYYY_When_it_is_not_logged(self):
        fileFullPath = self.getFilePath('metallica_fuell.mp3')
        files= {'file': open(fileFullPath, 'rb')}
        putData = {'trackName': 'Tema 1', 'owner': 'JoseYYY'}
        addTrackReq = requests.post('http://localhost:8080/apiv1/tracks', files=files,data=putData)

        self.assertEqual(403,addTrackReq .status_code)
        self.assertEqual('Forbidden',addTrackReq .reason)
        self.assertEqual('User invalid or not loggedin',addTrackReq .text)

    def test_get_existent_track_by_id(self):
        createJosePerez()
        logJosePerez()
        postData = {'trackName': 'Tema 1', 'owner': 'JoseYYY'}
        fileFullPath = self.getFilePath('metallica_fuell.mp3')

        files = {'file': open(fileFullPath, 'rb')}
        addTrackReq = requests.post('http://localhost:8080/apiv1/tracks', data=postData, files=files)

        getTrackReq = requests.get('http://localhost:8080/apiv1/tracks/Tema 1')
        self.assertEqual(getTrackReq.status_code, 200)
        self.assertEqual(getTrackReq.reason, 'OK')
        jsonResponse = json.loads(getTrackReq.text)
        self.assertTrue(len(jsonResponse),1)
        logoutJosePerez()


    def test_get_Nonexistent_track_by_id(self):
        getTrackReq = requests.get('http://localhost:8080/apiv1/tracks/Tema 2')
        self.assertEqual(getTrackReq.status_code, 200)
        self.assertEqual(getTrackReq.reason, 'OK')
        self.assertTrue(getTrackReq.content, 'No id was found')


    def test_get_two_tracks_with_substring_Tema(self):
        createJosePerez()

        fileFullPath = self.getFilePath('metallica_fuell.mp3')
        files = {'file': open(fileFullPath, 'rb')}
        logJosePerez()

        putData = {'trackName': 'Tema 1', 'fileContent': 'contenido', 'owner': 'JoseYYY'}
        addTrackReq = requests.post('http://localhost:8080/apiv1/tracks', data=putData, files=files)

        putData2 = {'trackName': 'Tema 2', 'fileContent': 'contenido2', 'owner': 'JoseYYY'}
        addTrackReq2 = requests.post('http://localhost:8080/apiv1/tracks', data=putData2, files=files)

        putData3 = {'trackName': 'Musica 1', 'fileContent': 'contenido3', 'owner': 'JoseYYY'}
        addTrackReq3 = requests.post('http://localhost:8080/apiv1/tracks', data=putData3, files=files)

        searchData = {'trackLikeName': 'Tema'}
        searchReq = requests.get('http://localhost:8080/apiv1/tracks',data = searchData)

        self.assertEqual(searchReq.status_code, 200)
        self.assertEqual(searchReq.reason, 'OK')
        jsonResponse = json.loads(searchReq.text)
        self.assertEqual(len(jsonResponse), 2)

        requests.delete('http://localhost:8080/apiv1/tracks/Tema 2')
        requests.delete('http://localhost:8080/apiv1/tracks/Musica 1')

        logoutJosePerez()

    @unittest.SkipTest
    def test_updateTrackWithNameTema1WhenIsLogged(self):
        createJosePerez()

        fileFullPath = self.getFilePath('metallica_fuell.mp3')
        files = {'file': open(fileFullPath, 'rb')}
        putData = {'trackName': 'Tema 1', 'fileContent': 'contenido', 'owner': 'JoseYYY'}
        addTrackReq = requests.post('http://localhost:8080/apiv1/tracks', json=putData, files=files )

        getTrackReq = requests.get('http://localhost:8080/apiv1/tracks/Tema 1')

        trackResponse = json.loads(getTrackReq.text, object_hook=lambda d: namedtuple('Track', d.keys())(*d.values()))

        self.assertEqual('Tema 1', trackResponse.track.trackName)
        self.assertEqual('contenido', trackResponse.track.fileContent)

        putJsonData = {'fileContent': 'nuevo contenido'}
        requests.put('http://localhost:8080/apiv1/tracks/Tema 1', json=putJsonData)
        secondGetAlbumReq = requests.get('http://localhost:8080/apiv1/tracks/Tema 1')
        secondAlbumResponse = json.loads(secondGetAlbumReq.text,
                                         object_hook=lambda d: namedtuple('Track', d.keys())(*d.values()))
        self.assertEqual('Tema 1', secondAlbumResponse.track.trackName)
        self.assertEqual('nuevo contenido', secondAlbumResponse.track.fileContent)

    def test_get_All_Tracks(self):
        createJosePerez()
        logJosePerez()
        putData = {'trackName': 'Tema 1', 'fileContent': 'contenido', 'owner': 'JoseYYY'}
        addTrackReq = requests.put('http://localhost:8080/apiv1/tracks', json=putData)

        putData2 = {'trackName': 'Tema 2', 'fileContent': 'contenido2', 'owner': 'JoseYYY'}
        addTrackReq2 = requests.put('http://localhost:8080/apiv1/tracks', json=putData2)

        putData3 = {'trackName': 'Musica 1', 'fileContent': 'contenido3', 'owner': 'JoseYYY'}
        addTrackReq3 = requests.put('http://localhost:8080/apiv1/tracks', json=putData3)

        searchReq = requests.get('http://localhost:8080/apiv1/tracks')

        self.assertEqual(searchReq.status_code, 200)
        self.assertEqual(searchReq.reason, 'OK')
        jsonResponse = json.loads(searchReq.text)
        #self.assertEqual(len(jsonResponse), 3)

        requests.delete('http://localhost:8080/apiv1/tracks/Tema 2')
        requests.delete('http://localhost:8080/apiv1/tracks/Musica 1')
        logoutJosePerez()

    def tearDown(self):
        requests.delete('http://localhost:8080/apiv1/users/JoseYYY')
        requests.delete('http://localhost:8080/apiv1/tracks/Tema 1')

if __name__ == '__main__':
    unittest.main()
