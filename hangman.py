import random
score = 10
true_chars = []
words = ['tree','clock','apple','python','bach','book','android']
words = random.choice(words)#apple

while true:

    for i in range(len(words)):
        if words[i] in true_chars:
            print(words[i],end = '')
        else:
            print('-', end=' ')
    char = input(' \n pleass enter a charecter:')

    if char in words:
        true_chars.append(char)
    else:
        score -=1
    print(score)

    #if true_chars == words:

    if score == 0:
        print("game over")
        break
