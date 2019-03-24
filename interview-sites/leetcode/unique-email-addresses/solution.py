# https://leetcode.com/problems/unique-email-addresses

from string import ascii_lowercase, digits

class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        for i, email in enumerate(emails):
            new_email = []
            local = True
            plus_found = False
            for letter in email:
                # When in the local name...
                if local:
                    # When still in the local name, and a plus has been found
                    if plus_found:
                        if letter == '@':
                            new_email.append(letter)
                            local = False
                            
                    # When still in the local name, before a plus has been found
                    elif letter in ascii_lowercase or letter in digits:
                        new_email.append(letter)
                    elif letter == '@':
                        new_email.append(letter)
                        local = False
                    elif letter == '+':
                        plus_found = True
                
                # When in the domain name...
                else:
                    new_email.append(letter)
            
            emails[i] = ''.join(new_email)
        
        print(emails)
        return len(set(emails))
