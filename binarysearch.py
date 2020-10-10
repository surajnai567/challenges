import time
arr = [i for i in range(1000000)]
l = 0
end = len(arr)
mid = int((l + end)/2)
start = time.time()
print(f'{time.time()-start}')

def bs(arr, n):
    if(arr[mid] == n):
        return mid
    if (arr[mid] < n):
        pass

import re

car = re.compile(r"(ha)+")
print(car.search("haha").group())

