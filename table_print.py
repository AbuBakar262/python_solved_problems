import json
import time
import numpy as np

start = time.time()

# read test.json in list type
with open('test.json', 'r') as f:
    data = f.readlines()

    arr = np.array(data)
    start = time.time()

    # np_arr= np.array([x for x in arr])

    # empty np array
    np_arr = np.empty(len(arr), dtype=object)

    for i, line in enumerate(arr):
        data = json.loads(line)