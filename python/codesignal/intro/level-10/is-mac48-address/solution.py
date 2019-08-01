# https://app.codesignal.com/arcade/intro/level-10/HJ2thsvjL25iCvvdm

import re

def isMAC48Address(s: str) -> bool:
    match = re.fullmatch('([0-9A-F]{2}\-){5}[0-9A-F]{2}', s)
    return bool(match)
