import requests
from dotenv import load_dotenv
import os 

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
    
    def getHeader(self):
        headers = {'Authorization': 'Bearer {token}'.format(token = self.getToken())}
        return headers
