# https://www.codewars.com/kata/human-readable-time/train/python

def make_readable(seconds):
    hours, seconds = divmod(seconds, 3600)
    minutes, seconds = divmod(seconds, 60)
    return f"{str(min(hours, 99)).rjust(2, '0')}:{str(minutes).rjust(2, '0')}:{str(seconds).rjust(2, '0')}"