from SpotifyAPI import SpotifyAPI

spotify = SpotifyAPI()
print(spotify.getToken) 
print(spotify.getHeader)
print(spotify.refreshToken)