# Write a program to accept a string from the user and display characters that are present at an even index number.
text = input('insert word: ')
n = 0
for i in text:
   if n % 2 == 0:
     print(text[n])
   n += 1
   
# the version of shown 

word = input('input word: ')
len_of_word = len(word)
for i in list(range(0,len_of_word,2)):
    print(word[i])