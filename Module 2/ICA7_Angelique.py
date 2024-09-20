
# empty list
emptyList = []
print(emptyList)

# numlist of 10 elements
numList = [ 10, 20, 30, 40, 50, 60, 70, 80, 90, 100 ]
print(numList[5])

# insert number 25 between 20 and 30
numList.insert(2, 25)
print(numList)

# insert number 75 between 70 and 80
numList.insert(8, 75)
print(numList)

# Print the index [5] and the length of this updated list
print(numList[5])

# Create a list named wordlist, containing the words “one, two, three, …” up to ten
wordList = [ "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten" ]

# Using indexing (with a colon), get the sublist containing the words “four, five six” and print this list.
print(wordList[3:6])

# Create a second word list containing the words “eleven, twelve, thirteen, fourteen, fifteen”
wordList2 = [ "eleven", "twelve", "thirteen", "fourteen", "fifteen" ]

# Combine these two lists together into a new list of 15 words.
combinedList = wordList + wordList2
print(combinedList)

# Pop() the word “ten” and print it out.
popWord = combinedList.pop(9)

# Pop() the last word and print it out.
popLastWord = combinedList.pop()