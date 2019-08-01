# https://leetcode.com/problems/unique-email-addresses

class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        for i, email in enumerate(emails):
            new_email = []
            local, domain = email.split('@')
            local = local.split('+')[0]
            local = local.replace('.', '')

            emails[i] = local + domain

        return len(set(emails))
