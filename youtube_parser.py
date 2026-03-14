from pytubefix import Playlist

def get_playlist_length(url):

    playlist = Playlist(url)

    return len(playlist.video_urls)