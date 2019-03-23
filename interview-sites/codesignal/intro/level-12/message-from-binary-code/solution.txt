# https://app.codesignal.com/arcade/intro/level-12/sCpwzJCyBy2tDSxKW

def messageFromBinaryCode(code):
    partitioned_code = []
    
    # Seperate into segments of 8
    for i in range(0, len(code), 8):
        partitioned_code.append(code[i:i+8])
    
    # Convert each partition into a symbol
    for i in range(len(partitioned_code)):
        p = partitioned_code[i]
        symbol = chr( int(''.join(p), base=2) )
        partitioned_code[i] = symbol
        
    return ''.join(partitioned_code)
