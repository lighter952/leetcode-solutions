def maxRepeating(sequence: str, word: str) -> int:
    count = 0
    if len(sequence) > 1:
        for i in range(0, len(sequence) - 1):
            if sequence[i] == word[0] and sequence[i + 1] == word[1]:
                count += 1
        return count
    elif sequence == word:
        return 1

print(maxRepeating('a', 'a'))