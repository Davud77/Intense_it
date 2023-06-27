def palindrome(word=""):
    return word == word[::-1]

print(palindrome("текст"))
print(palindrome("шалаш"))