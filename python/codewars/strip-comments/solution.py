# https://www.codewars.com/kata/strip-comments/train/python

def solution(string,markers):
    arr = string.split('\n')
   
    for i in range(len(arr)):
        comment_indices = [arr[i].find(m) for m in markers if arr[i].find(m) > -1]
        
        if comment_indices:
            comment_index = min(comment_indices)
            arr[i] = arr[i][:comment_index]
        else:
            comment_index = -1
        
        arr[i] = arr[i].rstrip(' ')
        
    result = '\n'.join(arr)
    return result
