# https://app.codesignal.com/arcade/intro/level-11/o2uq6eTuvk7atGadR

def lineEncoding(s):
    record = []
    record.append([])
    
    for letter in s:
        if len(record[-1]) == 0 or record[-1][0] == letter:
            record[-1].append(letter)
        else:
            record.append([letter])
            
    return ''.join( {1: ''}.get( len(i), str(len(i)) ) + i[0] for i in record ) 
