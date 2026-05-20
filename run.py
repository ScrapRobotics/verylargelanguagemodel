import json
import sys
import os
import random
from rich import print
from pathlib import Path
def smartTitle(word):
    if(word.title()==word):
        return word
    temp = ""
    for x in range(len(word)):
        if x==0:
            temp+=word[x].capitalize()
        else:
            temp+=word[x]
    return temp
os.chdir(sys.path[0])
with open(Path('data.json'), "r") as our_file:
    training = json.loads(our_file.read())
prompt = input("ScrapGPT Will Fill In Your Sentences . Be Sure To Format It Like This : ")
length = int(input("How many sentences? "))
starterword = smartTitle(prompt.split()[-1])
current = random.choice(training[starterword])
counter = 0
print(prompt, end="")
while counter < length:
    if(current not in "!?."):
        print(" "+current,end="")
    else:
        print(current,end="")
        counter+=1
    if current not in training.keys():
        print("[red]***ENCOUNTERED WORD NOT IN DATA***")
        break
    current = random.choice(training[current])

