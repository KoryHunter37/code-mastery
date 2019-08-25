# https://app.codesignal.com/interview-practice/task/pMvymcahZ8dY4g75q

def firstDuplicate(a):
    record = set()
    for i in a:
        if i in record:
            return i
        else:
            record.add(i)
    
    return -1