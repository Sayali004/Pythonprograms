text = input("Enter a paragraph:\n")

words = text.split()
print("\nTotal words:", len(words))

freq = {}
for word in words:
    word = word.lower()
    if word in freq:
        freq[word] += 1
    else:
        freq[word] = 1

print("\nWord frequencies:")
for word in freq:
    print(word, ":", freq[word])
    
print("\nTop 3 most frequent words:")

temp_freq = freq.copy()

for i in range(3):
    if temp_freq:
        max_word = ""
        max_count = 0
        for word in temp_freq:
            if temp_freq[word] > max_count:
                max_word = word
                max_count = temp_freq[word]
        print(max_word, ":", max_count)
        del temp_freq[max_word]

vowels = "aeiouAEIOU"
vowel_count = 0
for char in text:
    if char in vowels:
        vowel_count += 1

print("\nTotal vowels:", vowel_count)
