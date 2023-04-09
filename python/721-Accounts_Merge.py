# https://leetcode.com/problems/accounts-merge/


class UnionFind:

    def __init__(self, n: int):
        self.parents = list(range(n))

    def find(self, k: int):
        if self.parents[k] != k:
            self.parents[k] = self.find(self.parents[k])
        return self.parents[k]

    def union(self, k1: int, k2: int):
        self.parents[self.find(k1)] = self.find(k2)


def accountsMerge(accounts: list):
    emailIndex = dict()
    emailName = dict()

    for account in accounts:
        name = account[0]
        for email in account[1:]:
            if emailIndex.get(email, None) is None:
                emailIndex[email] = len(emailIndex)
                emailName[email] = name

    uf = UnionFind(len(emailIndex))

    for account in accounts:
        first_email = account[1]
        for email in account[2:]:
            uf.union(emailIndex[email], emailIndex[first_email])

    merge_emails = dict()
    for email, index in emailIndex.items():
        index = uf.find(index)
        merge_emails.setdefault(index, [])
        merge_emails[index].append(email)

    ans = []
    for email_list in merge_emails.values():
        ans.append([emailName[email_list[0]]] + sorted(email_list))

    return ans


if __name__ == "__main__":
    accounts = [["John", "johnsmith@mail.com", "john_newyork@mail.com"],
                ["John", "johnsmith@mail.com", "john00@mail.com"],
                ["Mary", "mary@mail.com"], ["John", "johnnybravo@mail.com"]]
    print(accountsMerge(accounts))
