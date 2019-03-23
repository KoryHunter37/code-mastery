# https://app.codesignal.com/arcade/intro/level-12/sqZ9qDTFHXBNrQeLC

import re
from collections import namedtuple
from typing import List, NamedTuple

class File_Name(NamedTuple):
    name: str
    identifier: List[int]

def fileNaming(names: List[str]) -> str:
    matches = re.findall(r'(\w+ *)((?:\(\w+\))*)', '\n'.join(names))
    file_names = []
    
    for match in matches:
        identifiers = [int(i) for i in match[1].replace(')', '').replace('(', ' ').split()]
        file_names.append([match[0], identifiers])
         
    print(file_names)
    for i, f in enumerate(file_names):
        if i == 0:
            continue
            
        candidate_files = [file_name for file_name in file_names[:i] if f[0] == file_name[0]]
        
        if f in candidate_files:
            if len(f[1]) == 0:
                f[1] = [1]
            else:
                f[1].extend([1])

            while f in candidate_files:
                f[1][-1] += 1
                
        names[i] = f[0]
        for number in f[1]:
            names[i] += f'({number})'
    
    return names
