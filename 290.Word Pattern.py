def wordPattern(pattern: str, word: str) -> bool:
    word = word.split(' ')
    if len(set(pattern)) != len(set(word)):
        False
    else:
        l = []
        for j in set(word):
            l.append([i for i, e in enumerate(word) if e == j])
            
        l2 = []
        for j in set(pattern):
            l2.append([i for i, e in enumerate(pattern) if e == j])

        for l_2 in l2:
            if l_2 not in l:
                return False
        return True