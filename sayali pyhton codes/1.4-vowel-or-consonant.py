c = str(input("Enter a character: "))
if c in 'aeiou':
    print("The character is a vowel")
elif c in 'bcdfghjklmnpqrstvwxyz':
    print("The character is a consonant")
else:
    print("The character is neither a vowel nor a consonant")