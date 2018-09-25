"""
stringjumble.py
Author: Jack Meehan
Credit: https://stackoverflow.com/questions/931092/reverse-a-string-in-python
https://stackoverflow.com/questions/4481724/convert-a-list-of-characters-into-a-string
Assignment:
The purpose of this challenge is to gain proficiency with 
manipulating lists.
Write and submit a Python program that accepts a string from 
the user and prints it back in three different ways:
* With all letters in reverse.
* With words in reverse order, but letters within each word in 
  the correct order.
* With all words in correct order, but letters reversed within 
  the words.
Output of your program should look like this:
Please enter a string of text (the bigger the better): There are a few techniques or tricks that you may find handy
You entered "There are a few techniques or tricks that you may find handy". Now jumble it:
ydnah dnif yam uoy taht skcirt ro seuqinhcet wef a era erehT
handy find may you that tricks or techniques few a are There
erehT era a wef seuqinhcet ro skcirt taht uoy yam dnif ydnah
"""
a = str(input('Please enter a string of text (the bigger the better):'))+(' ')
print('You entered "' + a + '". Now jumble it:')

b = (a[::-1]).strip()
print(b.lstrip())

words = []
word = " "
for i in a:
    if i == ' ':
        words.append(word)
        word = ""
    else:
        word = word + i
print(' '.join(words[::-1]))

smiles = []
smile = " "
for j in a:
    if j == ' ':
        smiles.append(smile)
        smile = ""
    else:
        smile = smile + j
f = (' '.join(smiles[::-1]))
print(''+ f[::-1])





