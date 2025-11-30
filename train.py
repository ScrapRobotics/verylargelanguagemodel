import json
import sys
import os
from pathlib import Path
os.chdir(sys.path[0])
data = []
training = {}
with open(Path('data.txt'), "r") as our_file:
    data = our_file.read().split()
for x in range(len(data)-1):
    if data[x] not in training.keys():
        training[data[x]] = [data[x+1]]
    else:
        training[data[x]].append(data[x+1])
with open(Path("data.json"), "w") as file:
    file.write(json.dumps(training))
print("Successfully trained model from data.txt! Raw data can be viewed in data.json.")