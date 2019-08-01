# https://app.codesignal.com/arcade/intro/level-6/6cmcmszJQr6GQzRwW

def evenDigitsOnly(n):
    return all( int(i) % 2 == 0 for i in str(n) )