class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        # we can have a dict:
        # {account_name: [set(emails), ...]}
        # so now for every new set of emails for given account name
        # we will check sets if emails, and union them

        acc = {}

        for name, *emails in accounts:
            emails = set(emails)
            if name not in acc:
                acc[name] = [emails]
                continue
            _emails = []
            for ac_emails in acc[name]:
                if emails.intersection(ac_emails):
                    emails = emails | ac_emails
                else:
                    _emails.append(ac_emails)
            _emails.append(emails)
            acc[name] = _emails
        
        res = []
        for name, accounts in acc.items():
            for emails in accounts:
                res.append([name, *list(emails)])
        
        return res
