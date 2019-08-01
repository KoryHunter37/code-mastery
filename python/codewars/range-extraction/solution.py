# https://www.codewars.com/kata/range-extraction/train/python

def solution(args):
    result = []
    
    def process_seq(seq):
        if len(seq) >= 3:
            result.append(str(seq[0]) + '-' + str(seq[-1]))
        else:
            for e in seq:
                result.append(str(e))
    
    
    seq = []
    for i in args:
        if len(seq) == 0:
            seq.append(i)
        elif i == seq[-1] + 1:
            seq.append(i)
        else:
            process_seq(seq)
            seq = [i]
            
    process_seq(seq)
            
    return ','.join(result)
