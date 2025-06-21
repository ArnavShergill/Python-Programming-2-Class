import formatting as f

f.title("Independent Practice #25")

f.dash()

f.section("Program 1")

quote = "Success is not final, falue is not fatal: it is the courage to continue that counts"
print(quote[:5])
print(quote[-5:])
print(quote[5:-2:4])

f.dash()

f.section("Program 2")

quote = "Be the change you wish to see in the world"
quote_list = quote.split(" ")
found_word = False

# Uses both types of loops. If found_word is true, then it will break out of all of the loops.
while found_word == False:
    for word in quote_list:
        if word == "change":
            print("change is present in the quote")
            found_word = True
            break
        else:
            print("change is not present in the quote")

f.dash()

f.section("Program 3")

quote = "the only way to do great work is to love what you do."
quote = quote[0].upper() + quote[1:]
print(quote)

"""The concept of string immutability is the ability to change different string components like whether each word is capitalized, if all of the words are lowercase or uppercase, etc.
The reason that the modification did not work just using indexing was because if one were to do this, the code would give them a TypeError, which is why I did the modification the way that I did."""

f.dash()
