from spotipy import Spotify


class LibraryService:
    client = None

    def __init__(self, access_token):
        self.client = Spotify(access_token)

    def get_all_tracks(self):
        offset = 0
        limit = 50
        tracks = []

        while True:
            response = self.client.current_user_saved_tracks(limit=limit, offset=offset)

            if len(response['items']) == 0:
                break

            tracks.extend(response['items'])

            offset += limit

        return tracks

    """
    filter tracks by genre given a list
    of genre names and tracks
    """

    def filter_by_genre(self, tracks, genre_names):
        tracks_filtered = []

        for track_item in tracks:
            track = track_item['track']
            for artist in track['artists']:
                artist_details = self.client.artist(artist['id'])
                if any(name in artist_details['genres'] for name in genre_names):
                    tracks_filtered.append(track)
                    break

        return tracks_filtered

    def filter_by_rock(self, tracks):
        return self.filter_by_genre(tracks, ['rock', 'hard rock', 'metal', 'punk', 'grunge', 'rock-and-roll'])

    def filter_by_edm(self, tracks):
        return self.filter_by_genre(tracks, ['edm', 'electronic', 'house', 'techno', 'trance'])

    def filter_by_pop(self, tracks):
        return self.filter_by_genre(tracks, ['pop', 'dance', 'r&b', 'soul', 'funk'])

    def filter_by_hip_pop(self, tracks):
        return self.filter_by_genre(tracks, ['hip-hop', 'rap', 'trap', 'r-n-b', 'rhythm-and-blues'])

    """
    remove all tracks from a playlist
    """
    def clear_playlist(self, playlist_id):
        try:
            self.client.playlist_replace_items(playlist_id, [])
        except Exception as e:
            return e

        return None

    def add_tracks_to_playlist(self, playlist_id, rock_tracks):
        try:
            self.client.playlist_add_items(playlist_id, rock_tracks)
        except Exception as e:
            return e

        return None
