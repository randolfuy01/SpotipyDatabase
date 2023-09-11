import requests
from dotenv import load_dotenv
import os 
import base64

class SpotifyAPI:
    
    def __init__(self) -> None:

        load_dotenv()
        self.clientID = os.getenv("Client_ID")
        self.clientSecret = os.getenv("Client_Secret")

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
    
    def refreshToken(self):
        authclient = self.clientID + ":" + self.clientSecret
        authEncode = 'Basic ' + base64.b64encode(self.clientID()).decode()
        headers = {
            'Authization': authEncode
        }

        data = {
            'grant_type' : 'refresh_token',
            'refresh_token' : self.getToken()
        }

        response = requests.post('https://accounts.spotify.com/api/token', data=data, headers=headers)

    def getHeader(self):
        headers = {'Authorization': 'Bearer {token}'.format(token = self.getToken())}
        return headers
    
