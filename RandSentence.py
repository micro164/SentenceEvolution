#Sentence Evolution

import string
import random
import time

characters = string.ascii_lowercase + string.ascii_uppercase + string.digits + ' .,|?;:' #All possible characters
sentence = input("Enter text: ") #message to be matched
Cur = ''.join(random.choice(characters) for i in range(len(sentence))) #populate initial generation with random characters
Nxt = ''
complete = False
gen = 0

while complete == False:
    print(Cur)
    Nxt = ''
    complete = True
    for i in range(len(sentence)):
        if Cur[i] != sentence[i]:
            complete = False
            Nxt += random.choice(characters)
        else:
            Nxt += sentence[i]  
    gen += 1
    Cur = Nxt

print("Generations:" + str(gen))
