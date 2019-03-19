# https://app.codesignal.com/arcade/intro/level-6/6Wv4WsrsMJ8Y2Fwno

from string import ascii_letters, digits

def variableName(name):
    return all([i in ascii_letters + digits + '_' for i in name]) and name[0] not in digits
