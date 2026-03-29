class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        hashset = set()


        for email in emails:
            for i in range(len(email)):
                if email[i] == "@":
                    domain_name = email[i:]
                    local_name = email[:i].replace(".", "")

                    if "+" not in local_name:
                        hashset.add(local_name + domain_name)
                    else:
                        for j in range(len(local_name)):
                            if local_name[j] == "+":
                                adjusted_name = local_name[:j] + domain_name
                                hashset.add(adjusted_name)
                                break
        return len(hashset)
