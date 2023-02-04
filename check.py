# write code to check the length of json file

import json
import os

data = json.load(open('data/scienceQ.json'))
print(len(data))
