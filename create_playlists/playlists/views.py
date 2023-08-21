import os

from django.http import JsonResponse

from create_playlists.services.libraryService import LibraryService


def rock(request):
    access_token = request.session['access_token']
    library_service = LibraryService(access_token)

    # get all tracks from user's library
    all_tracks = library_service.get_all_tracks()

    # filter tracks by rock genre
    rock_tracks = library_service.filter_by_rock(all_tracks)

    playlist_id = os.getenv('rock_playlist_id')

    if not playlist_id:
        return JsonResponse({'error': 'No playlist id found'}, status=500)

    # clear playlist if already have some tracks
    error_clear_playlist = library_service.clear_playlist(playlist_id)

    if error_clear_playlist:
        return JsonResponse({'error': error_clear_playlist}, status=500)

    # add tracks to playlist
    error_add_tracks_playlist = library_service.add_tracks_to_playlist(playlist_id, rock_tracks)

    if error_add_tracks_playlist:
        return JsonResponse({'error': error_add_tracks_playlist}, status=500)

    return JsonResponse({'success': True})


def edm(request):
    return None


def pop(request):
    return None


def hip_pop():
    return None
