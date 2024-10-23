words = ["bread", "cheese", "fry", "fish", "holistic", "abstract", "reign", "ready"]

nr_words_5 = 0
for word in words:
    if len(word) == 5:
        nr_words_5 += 1
    else:
        continue        
    
print("The number of words with 5 characters in the list provided is:", nr_words_5)