# https://leetcode.com/problems/word-ladder-ii/


def findLadders(beginWord: str, endWord: str, wordList: list):

    ans = []
    adj = dict()
    if beginWord not in wordList:
        wordList = [beginWord] + wordList

    for i in range(len(wordList)):
        adj.setdefault(wordList[i], [])

    for i in range(len(wordList)):
        cur_word = wordList[i]
        for j in range(len(cur_word)):
            for k in range(97, 123):
                new_word = cur_word[:j] + chr(k) + cur_word[j + 1:]
                if adj.setdefault(new_word,
                                  None) is not None and new_word != cur_word:
                    adj[cur_word].append(new_word)
                elif new_word != cur_word:
                    del adj[new_word]

    l1 = [beginWord]
    l2 = []
    depth = {beginWord: 1}
    visited = {beginWord: 1}
    shortest = 1

    while len(l1) > 0:
        cur_word = l1.pop(0)
        if endWord in adj[cur_word]:
            shortest += 1
            break

        i = 0
        while i < len(adj[cur_word]):
            if not visited.setdefault(adj[cur_word][i], 0):
                visited[adj[cur_word][i]] = 1
                l2.append(adj[cur_word][i])
                depth[adj[cur_word][i]] = shortest + 1
                i += 1
            elif depth[adj[cur_word][i]] <= shortest:
                del adj[cur_word][i]
            else:
                i += 1

        if len(l1) == 0:
            l1, l2 = l2, l1
            shortest += 1

    depth[endWord] = shortest

    def dfs(word: str, path: list, count: int):
        count += 1
        if count > shortest or count > depth.setdefault(word, float("inf")):
            return
        if word == endWord:
            ans.append(path)
            return

        for each in adj.setdefault(word, []):
            if each not in path:
                path_cp = path.copy()
                path_cp.append(each)
                dfs(each, path_cp, count)

    dfs(beginWord, [beginWord], 0)

    return ans


if __name__ == "__main__":
    wordList = ["ted", "tex", "red", "tax", "tad", "den", "rex", "pee"]
    print(findLadders('red', 'tax', wordList))
