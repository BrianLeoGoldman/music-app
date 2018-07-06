import requests
def createAlbumXToJose():
    albumJsonData = {'name': 'AlbumX',
                     'year': '2010',
                     'owner': 'JoseYYY'}
    addAlbumReq = requests.put('http://localhost:8080/apiv1/albums', json=albumJsonData)
    return addAlbumReq


def logoutJosePerez():
    jsonData = {'userName': 'JoseYYY'}
    requests.post('http://localhost:8080/apiv1/logout', json=jsonData)


def logJosePerez():
    jsonData = {'password': 'Clave1234._5'}
    requests.post('http://localhost:8080/apiv1/login/JoseYYY', json=jsonData)
    
def logMaxPowell():
    jsonData = {'password': 'Password1234'}
    requests.post('http://localhost:8080/apiv1/login/Max01', json=jsonData)


def createJosePerez():
    jsonData = {'name': 'Jose',
                'lastName': 'Perez',
                'userName': 'JoseYYY',
                'password': 'Clave1234._5'}
    requests.put('http://localhost:8080/apiv1/users', json=jsonData)
    
def createMaxPowell():
    jsonData = {'name': 'Max',
                'lastName': 'Powell',
                'userName': 'Max01',
                'password': 'Password1234'}
    requests.put('http://localhost:8080/apiv1/users', json=jsonData)


def createAlbumYToJose():
    albumJsonData = {'name': 'AlbumY',
                     'year': '2012',
                     'owner': 'JoseYYY'}
    addAlbumReq = requests.put('http://localhost:8080/apiv1/albums', json=albumJsonData)
    return addAlbumReq
