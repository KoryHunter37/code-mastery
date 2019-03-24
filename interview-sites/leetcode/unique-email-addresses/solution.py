# https://leetcode.com/problems/unique-email-addresses

from string import ascii_lowercase, digits

class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        for i, email in enumerate(emails):
            new_email = []
            local, domain = email.split('@')
            for letter in local:                        
                if letter in ascii_lowercase or letter in digits:
                    new_email.append(letter)
                elif letter == '+':
                    break
                    
            new_email.extend(domain) 
            
            emails[i] = ''.join(new_email)

        return len(set(emails))
                    