word = "YOKOHAMA"  # String instead of list
guess = "YOKOHAMA"

for i in range(len(word)):
    if word[i] == guess[i]:
        print(f"Correct letter at position {i}: {word[i]}")