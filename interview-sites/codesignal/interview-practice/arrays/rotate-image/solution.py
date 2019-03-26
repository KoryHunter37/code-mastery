# https://app.codesignal.com/interview-practice/task/5A8jwLGcEpTPyyjTB

from typing import List

def rotateImage(a: List[List[int]]) -> List[List[int]]:
    return [[a[i][j] for i in range(len(a[0]))][::-1] for j in range(len(a))]
