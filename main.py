# largest palindromic product of two three-digit numbers

palindromes = []

for i in range(100, 1000):
    for n in range(100, 1000):
        result = str(i * n)
        reverseResult = str(i * n)[::-1]
        if result == reverseResult:
            palindromes.append(int(result))

palindromesSorted = sorted(palindromes)
print(palindromesSorted[-1])