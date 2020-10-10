import string
import random
import time
alphabets = string.printable[10:36]


def measure_time(fun):
  def wrapper(*args, **kwargs):
    start = time.time()
    res = fun(*args, **kwargs)
    end = time.time()
    print(end-start)
    return res
  return wrapper


def create_word():
  return "".join([random.choice(alphabets) for i in range(5)])


words = [create_word() for i in range(1000000)]


@measure_time
def sentance(words):
  sentance = ''
  for i in words:
    sentance +=i
  return sentance


@measure_time
def builder():
  return "".join(words)


print("not builder", sentance(words))
print('builder', builder())

