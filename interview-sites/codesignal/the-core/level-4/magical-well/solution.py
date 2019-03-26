# https://app.codesignal.com/arcade/code-arcade/loop-tunnel/LbuWRHnMoJH9SAo4o

def magicalWell(a, b, n):
    return sum((a+i) * (b+i) for i in range(n))
