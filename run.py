import json
import sys
import os
import random
from rich import print
from pathlib import Path
os.chdir(sys.path[0])
with open(Path('data.json'), "r") as our_file:
    training = json.loads(our_file.read())
prompt = input("ScrapGPT Will Fill In Your Sentences . Be Sure To Format It Like This : ")
length = int(input("How many sentences? "))
starterword = prompt.split()[-1].title()
current = starterword
counter = 0
print(prompt, end=" ")
while counter < length:
    if current not in training.keys():
        print("[red]***ENCOUNTERED WORD NOT IN DATA***")
        break
    next = random.choice(training[current])
    print(next, end=" ")
    current = next
    if next in "!?.":
        counter+=1
