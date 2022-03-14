#Script loads json file as dictionary and removes all words of length different than 5
import json

with open('words_dictionary.json') as json_file:
    data = json.load(json_file)
    #print("Type:", type(data))

keys_to_delete = []

keys = data.keys()

# Mark letters with len different than 5 for deletion
for key in keys:
    if len(key) != 5:
        keys_to_delete.append(key)

# Delete marked keys
for i in range(len(keys_to_delete)):
    del data[keys_to_delete[i]]

keys = data.keys()

#Wipe the contents of 5_letter_words.txt
open('5_letter_words.txt', 'w').close()

#Append dictionary keys to the 5_letter_word file
with open('5_letter_words.txt', 'a') as file:
    for key in keys:
        file.write(key)
        file.write('\n')