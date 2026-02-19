class Solution:
    def isAnagram(s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        hashset_s = set()
        hashset_t = set()

        letter_s = list(s)
        letter_t = list(t)

        for letter in letter_s:
            if letter in hashset_s:
                hashset_s[letter] += 1
            else:
                hashset_s[letter] = 1
        
        for letter in letter_t:
            if letter in hashset_t:
                hashset_t[letter] += 1
            else:
                hashset_t[letter] = 1
        
        if hashset_s == hashset_t:
            return True
        else:
            return False