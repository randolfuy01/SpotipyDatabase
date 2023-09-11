import requests
class SpotifyAPI:
    
    def __init__(self) -> None:
        self.clientID = ""
        self.clientSecret = ""

    def getToken(self):
        authUrl = 'https://accounts.spotify.com.api/token'

        authResponse = requests.post(authUrl, {
            'grant_type': 'client_credentials',
            'client_id' : self.clientID,
            'client_secret' : self.clientSecret
        })

        authResponseData = authResponse.json()
        accessToken = authResponseData['access_token']
        return accessToken
    
    def getHeader(self):
        headers = {'Authorization': 'Bearer {token}'.format(token = self.getToken())}
        return headers
