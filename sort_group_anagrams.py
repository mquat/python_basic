import collections

from typing import List

## Simple example of collections.defaultdict

strs = ['a', 'b', 'c', 'd']

result = collections.defaultdict(list)

for word in strs:
    result[word].append(word)

print(result)                   # defaultdict(<class 'list'>, {'a': ['a'], 'b': ['b'], 'c': ['c'], 'd': ['d']})
print(result.values())          # dict_values([['a'], ['b'], ['c'], ['d']])
print(dict(result.items()))     # {'a': ['a'], 'b': ['b'], 'c': ['c'], 'd': ['d']}



## Anagrams

def groupAnagrams(strs: List[str]) -> List[List[str]]:
    anagrams = collections.defaultdict(list)

    for word in strs:
        anagrams[''.join(sorted(word))].append(word)    #sorted(word)를 key로 잡고, sorted(word)가 동일하면 해당 key로 append 한다 

    return list(anagrams.values())

strs = ["eat", "tea", "tan", "ate", "nat", "bat"]

print(groupAnagrams(strs))