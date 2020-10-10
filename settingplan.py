manager_position = []
all_vacant_position = []
pos = ['OOOO OOOM',
'OVOO OOOO',
'OOVO OOVO',
'OOOO OOOO',
'OOOO OOOO',
'OOOO OOOO',
'OOOO OOOO',
'OOOO VOOO']


def find_vacant(rows):
    for i,row in enumerate(rows):
        for j, col in enumerate(row):
            if col == 'M':
                manager_position.append((i+1, j if j > 4 else j+1))

            if col == 'V':
                all_vacant_position.append((i+1, j if j > 4 else j+1))

def find_minimum():
    min = 10000
    for vacant in all_vacant_position:
        if abs(manager_position[0][1] - vacant[1]) > 4:
            a = abs(manager_position[0][1] - vacant[1]) - 1
            dis = abs(manager_position[0][0] - vacant[0]) + a
            if dis < min:
                min = dis + 2
        else:
            a = abs(manager_position[0][1] - vacant[1]) - 1
            dis = abs(manager_position[0][0] - vacant[0]) + a
            if dis < min:
                min = dis

    return min
find_vacant(pos)
print(find_minimum(), end="")
