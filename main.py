import random

N = 10000  # number of iterations


def nochange(a):
    random.shuffle(a)
    return a[random.choice([0, 1, 2])]


def changechoice(a):
    random.shuffle(a)
    first_i = a[random.choice([0, 1, 2])]
    opened_door = 0  # door opened by TV presenter

    for i in range(3):
        if i != first_i and a[i] == 0:
            opened_door = i
            break
    
    for i in range(3):
        if i != opened_door and i != first_i:
            return a[i]


cnt = 0
cnt1 = 0

for i in range(N):
    arr = [0, 1, 0]  # 0 - goat, 1 - car

    if nochange(arr) == 1:
        cnt += 1

    if changechoice(arr) == 1:
        cnt1 += 1

print("No changed a door: - " + str((cnt / N) * 100) + "%")
print("With changed a door: - " + str((cnt1 / N) * 100) + "%")
