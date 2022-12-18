# Paste your code here
def song_playlist(songs, max_size):
    """
    songs: list of tuples, ('song_name', song_len, song_size)
    max_size: float, maximum size of total songs that you can fit
    Start with the song first in the 'songs' list, then pick the next 
    song to be the one with the lowest file size not already picked, repeat
    Returns: a list of a subset of songs fitting in 'max_size' in the order 
             in which they were chosen.
    """
    playlist = []
    if songs[0][2] <= max_size:
        playlist.append(songs[0][0])
    else:
        return playlist
    song_list_copy_ascending = sorted(songs, key = lambda x: x[2])
    song_list_copy_ascending.remove(songs[0])
    space_remain = max_size - songs[0][2]
    for i in song_list_copy_ascending:
        if i[2] <= space_remain:
            playlist.append(i[0])
            space_remain -= i[2]
        else:
            break
    return playlist
    