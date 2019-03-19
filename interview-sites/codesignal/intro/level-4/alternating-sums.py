# https://app.codesignal.com/arcade/intro/level-4/cC5QuL9fqvZjXJsW9

def alternatingSums(a):
    
    team_1 = [a[i] for i in range(len(a)) if i % 2 == 0]
    team_2 = [a[i] for i in range(len(a)) if i % 2 == 1]
    
    return [sum(team_1), sum(team_2)]
