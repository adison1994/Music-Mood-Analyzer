import json
import requests

# A simple class to store attributes of a single track.

class Track(object):
    def __init__(self, name, track_id, artist):
        # Name of the track (Can be used to display on the front end)
        self.name = name
        # ID of the track (Will be used to get the Lyrics)
        self.id = track_id
        # Name of the artist
        self.artist = artist

    def addLyrics(self, lyrics):
        # Variable storing lyrics of the current track.
        self.lyrics = lyrics

    def label(self, mood) :
        # This is to store the final label (Happy/Sad) after classification is complete.
        self.mood = mood


class Musix(object):
    def __init__(self, country="us", apikey="acf266ecb81687ee6f567e6fe9d0ca06"):
        # Country variable will be used for getting charts.
        self.country = country

        # Developer registration.
        self.apikey = apikey

    # Changing the country of search
    def change_country(self, country):
        self.country = country

    # Function to retrive lyrics of top k songs in a country.
    # Step 1 : Get the Songs/Tracks. Store their name and ID.
    # Step 2 : Get lyrics for each track using it's ID.
    def get_top_lyrics(self, k):

        # Get the songs.
        tracks = self.get_top_songs()

        # Get the Lyrics for first 'k' objects in the list.
        for track in tracks[:k]:
            track.addLyrics(self.get_lyrics(track.id))

        return tracks;


    # This function will get the top 'songs' of the desired country.
    def get_top_songs(self):
        # The URL for getting charts.
        url = "https://api.musixmatch.com/ws/1.1/chart.tracks.get"

        # Params for the Request
        querystring = {"format": "json", "callback": "callback",
                       "country": self.country, "apikey": self.apikey, "page_size":100,}
        headers = {'Accept': "text/plain", }

        # Perform Request and get the JSON response.
        response = requests.request("GET", url, headers=headers, params=querystring).json()

        # Iterate over the track list and extract the track names and track id's
        songs = []
        for track in response['message']['body']['track_list']:

            # Get the name
            name = track['track']['track_name']

            # Get the ID
            track_id = track['track']['track_id']

            # Get the artist name
            artist = track['track']['artist_name']
            
            # Create a Track Object
            trackObj = Track(name, track_id, artist)

            # Save the track object.
            songs.append(trackObj)

        return songs

    # Function to request for lyrics of the given track_id
    def get_lyrics(self, track_id):
        # URL to get the Lyrics
        url = "https://api.musixmatch.com/ws/1.1/track.lyrics.get"
        
        # Params for the reqest.
        querystring = {"format": "json", "callback": "callback",
                       "track_id": track_id, "apikey": self.apikey}
        headers = {'Accept': "application/json", }

        # Perform the Request
        response = requests.request("GET", url, headers=headers, params=querystring).json()

        # Extract and return the lyrics.
        # The reason I am using 'replace' function is because Musixmatch appends a string to the lyrics. 
        # We need to remove this because it will cause a problem in the classification.
        return response['message']['body']['lyrics']['lyrics_body'].replace("******* This Lyrics is NOT for Commercial use *******", "")
