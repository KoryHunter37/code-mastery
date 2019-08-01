# https://app.codesignal.com/arcade/code-arcade/book-market/MX94DWTrwQw2gLrTi

import re

def htmlEndTagByStartTag(startTag):
    pattern = re.compile(r'^<([^ ^>]+)')
    matches = pattern.findall(startTag)
    return f'</{matches[0]}>'
