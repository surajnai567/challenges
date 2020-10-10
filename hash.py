import hashlib

print(hashlib.algorithms_available)

md = hashlib.sha3_256('hello'.encode())
cd = hashlib.sha3_256('hello'.encode())

md.update('ani'.encode())
cd.update('ani'.encode())
print(md.hexdigest() == cd.hexdigest())

with open('hello', 'rb') as f:
  for line in f:
    print(line)
    md.update(line)

  print(len(md.hexdigest()))

print(len(hashlib.md5('hello'.encode()).hexdigest()))






