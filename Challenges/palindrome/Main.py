print("Welcome to the palindrome test")
word = input("Enter a word: ")
backwards = ""
# palindrome = False
# i = len(word) - 1
# while i >= 0:
#     backwards += word[i]
#     i -= 1
#
# if word.lower() == backwards.lower():
#     palindrome = True
#
# print(palindrome)

i = 0
j = len(word) - 1
palindrome = True
while i < len(word)/2:
    if word.lower()[i] == word.lower()[j]:
        i += 1
        j -= 1
        continue
    else:
        palindrome = False
        break

print(palindrome)