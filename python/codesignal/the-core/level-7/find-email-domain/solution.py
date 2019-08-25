# https://app.codesignal.com/arcade/code-arcade/book-market/TXFLopNcCNbJLQivP

import re

def findEmailDomain(address: str) -> str:
    pattern = re.compile(r'.*@(.*)$')
    matches = pattern.findall(address)
    return matches[0]
