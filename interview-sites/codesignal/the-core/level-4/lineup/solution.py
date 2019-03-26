# https://app.codesignal.com/arcade/code-arcade/loop-tunnel/8rqs3BLpdKePhouQM

def lineUp(commands):
    count = 0
    valid = True
    
    for command in commands:
        if command in 'LR':
            valid = not valid
            
        count += int(valid)
                
    return count
