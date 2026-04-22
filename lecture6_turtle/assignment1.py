
sentences = [

"Python is great and python is powerful",

"Java is powerful but verbose",

"Python and Java are popular languages",

"JavaScript is different from Java",

"Python python PYTHON everywhere" 

]
#convert each list object to lowercase and append to new_sentences
new_sentences = []
for i in sentences:
    i = i.lower()
    new_sentences.append(i)
word_count = 0
def finding_word(word):
    for x in sentences:
        for l in [0, len(new_sentences[x])]:
            if word in l:
                word_count += 1

finding_word("python")
print(f"The word 'python' is present {word_count} times.")
word_count = 0
finding_word("java")
print(f"The word 'java' is present {word_count} times.")
word_count = 0
finding_word("is")
print(f"The word 'is' is present {word_count} times.")