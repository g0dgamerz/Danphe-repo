
sentence = input("enter some text: ")

# using naive method to get count
# of each element in string
freq = {}

for i in sentence:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1

# printing result
print("Count of all characters in" + sentence +"is :\n" + str(freq))
