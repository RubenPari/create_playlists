import os

from django.http import HttpResponseRedirect, JsonResponse
from spotipy import SpotifyOAuth

scopes = os.getenv('SPOTIPY_SCOPES').split(',')
oauth = SpotifyOAuth(scope=scopes)


def login(request):
    auth_url = oauth.get_authorize_url()
    return HttpResponseRedirect(auth_url)


def callback(request):
    code = request.GET.get('code')
    token_info = oauth.get_access_token(code)

    # save access_token to session
    request.session['access_token'] = token_info['access_token']

    return JsonResponse({
        'status': 'success',
        'message': 'Successfully logged in'
    })


def logout(request):
    request.session.flush()

    return JsonResponse({
        'status': 'success',
        'message': 'Successfully logged out'
    })
