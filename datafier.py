import sys
import os
from pathlib import Path
os.chdir(sys.path[0])
newdata = ""
file = input("Enter Filename (be sure to add extension + ensure in same directory!): ")
with open(Path(file), "r") as our_file:
    data = our_file.read().title()
for x in data:
    if x in "!?.":
        newdata+=" "
    newdata+=x
if not (newdata[-1]==" "):
    newdata+=" "
with open(Path('data.txt'), "a") as f:
    f.write(newdata)