# https://app.codesignal.com/arcade/intro/level-3/9DgaPsE2a7M6M2Hu6

parentheses_reversal = str.maketrans("()", ")(")
parentheses_removal = str.maketrans("", "", "()")


def reverseInParentheses(inputString):
    print(inputString)
    if len(inputString) == 0:
        return ''
    
    if len(inputString.translate(parentheses_removal)) == 0:
           return ''
    

    depth = 0
    curr = []
    other = []
    for i, letter in enumerate(inputString):
        if letter == '(':
            depth += 1

        if depth > 0:
            other.append(letter)
        else:
            curr.append(letter)

        if letter == ')':
            depth -= 1
            if depth == 0:
                if other:
                    curr.extend(reverseInParentheses(''.join(other)[-2:0:-1].translate(parentheses_reversal)))
                    other = []
            

    if other:
        try:
            curr.extend(reverseInParentheses(''.join(other)[-2:0:-1].translate(parentheses_reversal)))
        except:
            pass

    return ''.join(curr)
