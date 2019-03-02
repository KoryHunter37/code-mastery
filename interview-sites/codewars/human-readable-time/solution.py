# https://www.codewars.com/kata/human-readable-time/train/python

def make_readable(seconds):
    hours, seconds = seconds // 3600, seconds % 3600
    minutes, seconds = seconds // 60, seconds % 60
    return f"{str(min(hours, 99)).rjust(2, '0')}:{str(minutes).rjust(2, '0')}:{str(seconds).rjust(2, '0')}"