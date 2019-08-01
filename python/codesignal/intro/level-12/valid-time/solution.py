# https://app.codesignal.com/arcade/intro/level-12/ywMyCTspqGXPWRZx5

import re

def validTime(s: str) -> bool:
    match = re.search(r'2[1-3]|[01][0-9]:[0-5][0-9]', s)
    
    return bool(match)
