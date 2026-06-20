s = "Was it a car or a cat i saw?"

for i in range(len(s)):
    letter = s[i]
    if letter == s[len(s)-1]:
        continue
    else:
        return False
    return True