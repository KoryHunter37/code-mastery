# https://app.codesignal.com/interview-practice/task/uX5iLwhc6L5ckSyNC

def firstNotRepeatingCharacter(s):
        
        for i in range(len(s)):
                letter = s[i]

                if letter not in s[:i] + s[i+1:]:
                        return letter
        return '_'