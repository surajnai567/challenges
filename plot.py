
def generate_map(x1, x2, y1, y2):
    return [(i, j) for i in range(x1, x2+1)
            for j in range(y1, y2+1)]

a = generate_map(1, 2, 1, 2)
b = generate_map(2, 4, 2, 4)

def block_count(map1, map2):
    count = 0
    for i in map2:
        if i in map1:
            count += 1
    return count

result = set()
bat = [(3, 100), (4, 300), (6, 200)]
cri = [(2, 300), (3, 200), (6, 100)]

def number_of_point(bat, cicket):
    for i, ba in enumerate(bat):
        for c in cicket:
            if ba[0] > c[0] and ba[1] <= c[1]:
                print(i)
                result.add(i)
number_of_point(bat, cri)
print(len(result))

