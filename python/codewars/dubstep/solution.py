# https://www.codewars.com/kata/dubstep/train/python

def song_decoder(song):
    song = song.replace('WUB', ' ')
    song = song.split()
    return ' '.join(song)
