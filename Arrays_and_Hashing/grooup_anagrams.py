def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        letter_map = []
        for word in strs:
            letters = sorted(list(word))
            letter_map.append(letters)
            for index, letter in enumerate(letter_map):
                print(index, letter)

groupAnagrams(["act","pots","tops","cat","stop","hat"])