import random
tries = 15
word = []
with open('words.txt', 'r')as words:
    for i in words.read().split(" "):
        i = i.split("\n")
        word.append(i)
word = word.pop(0)
print(word)
# for i,wo in enumerate(word[0]):
#     print(i,wo)
difficulty = input("pls enter difficulty\n 1 for easy\n 2 for medium\n 3 for nightmare\n4 for ultra nightmare\ntype anything for random: ")
if difficulty == "1":
    wordL = 4
    word4 = True
    while word4:
        wordIndexRandom = int(random.randint(0, 800))
        wordGenerated = word[wordIndexRandom]
        wordGENL = len(wordGenerated)
        if  wordGENL == wordL:
            word4 = False
elif difficulty =="2":
    wordL = 6
    tries = 7
    word4 = True
    while word4:
        wordIndexRandom = int(random.randint(0, 800))
        wordGenerated = word[wordIndexRandom]
        wordGENL = len(wordGenerated)
        if wordGENL == wordL:
            word4 = False

elif difficulty =="3":
    wordL = 11
    tries = 19
    word4 = True
    while word4:
        wordIndexRandom = int(random.randint(0, 800))
        wordGenerated = word[wordIndexRandom]
        wordGENL = len(wordGenerated)
        if wordGENL == wordL:
            word4 = False
elif difficulty =="4":
    wordL = 15
    tries = 15
    word4 = True
    while word4:
        wordIndexRandom = int(random.randint(0, 800))
        wordGenerated = word[wordIndexRandom]
        wordGENL = len(wordGenerated)
        if wordGENL == wordL:
            word4 = False

else:
    wordIndexRandom = int(random.randint(0, 800))
    wordGenerated = word[wordIndexRandom]
sovled = False
wordLenth = len(wordGenerated)
wordGenerated = list(wordGenerated)
wordFound = "_"*wordLenth
wordFound = list(wordFound)

while not sovled and tries >0:
    if not "_" in wordFound:
        sovled = True
        print("You Found The word Congracs")
        print(wordGenerated)
        break
    count = 0
    for i in wordFound:
        if i == "_":
            count+=1
            if count == wordLenth:
                for i in range(2):
                    rand = random.randint(0,wordLenth-1)
                    ind = wordGenerated[rand]
                    print(ind)
                    wordFound[rand] = ind
    try:
        print("tries = ",tries)
        print(wordFound)
        inp = input()
        tries -= 1
        for i in wordGenerated:
            if i == inp:
                inx = wordFound.index("_")
                index = wordGenerated.index(i,inx)
                wordFound[index] = i
    except ValueError:
        sovled = True
        print("You Found The word Congracs")
        print(wordGenerated)
        break
if tries == 0 and sovled==False:
    print("you lose")
    print(wordGenerated)