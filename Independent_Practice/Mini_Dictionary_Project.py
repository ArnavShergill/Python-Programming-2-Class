import formatting as f

f.clear_console()

f.title("Mini Project: Dictionaries")

f.short_dash()

f.section("Task 1 - Alphabetical Order")

user_sentence = input("Enter a sentence: ")
alphabet_list = {}
for character in user_sentence:
    alphabet_instance = user_sentence.find(character)#tries to find the index for the character in the list
    alphabet_list.update({character:alphabet_list.get(character,0)+1}) #updates the list

for key in alphabet_list:
    print(f"{key}: {alphabet_list[key]}")

f.dash()

f.section("Task 2 - Pirate Talk")

pre_translation = input("input a sentence without punctuation: ").lower().split(" ")#formats the input to become a list and every word is lowercase

pirate_translation = {"sir":"matey", "hotel":"fleabag inn", "student":"swabbie", "boy":"matey", "madam":"proud beauty", "professor":"foul blaggart", "restaurant":"galley", "your":"yer", "excuse":"arr", "students":"swabbies", "are":"be","lawyer":"foul blaggart", "the":"th'", "restroom":"head", "my":"me", "hello":"avast", "is":"be", "man":"matey"}

pre_translation_list = []

def translator(pre_translation):
    for word in pre_translation:
        if word in pirate_translation.keys():
            pre_translation_list.append(pirate_translation[word])#replaces the words found with the words in 'pirate_translation' into 'pre_translation_list'
        else:
            pre_translation_list.append(word) #keeps the words that are not found in the 'pirate_translation' into 're_translation_list'

translator(pre_translation)

print("\n" + " ".join(pre_translation_list))#prints as a sentence instead of a list
f.dash()
