class Solution:
    def anagrams(self, strs):
        d = collections.defaultdict(list)
        for st in strs:
            d[tuple(sorted(st))].append(st)
        return [word for anagram in d.values() if len(anagram) > 1 for word in anagram]
