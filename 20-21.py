# https://inf-ege.sdamgia.ru/problem?id=36033
def move1(num):
    return [num[0]+1, num[1]]


def move2(num):
    return [num[0]*2, num[1]]


def move3(num):
    return [num[0], num[1]+1]


def move4(num):
    return [num[0], num[1]*2]


def win(num):
    s = num[0] + num[1]
    return s >= 107


def game20(state_num, num):
    if state_num < 3 and win(num):
        return False
    elif state_num == 3:
        return win(num)
    if state_num % 2 == 0:
        return game20(state_num + 1, move1(num)) or \
               game20(state_num + 1, move2(num)) or \
               game20(state_num + 1, move3(num)) or \
               game20(state_num + 1, move4(num))
    else:
        return game20(state_num + 1, move1(num)) and \
               game20(state_num + 1, move2(num)) and \
               game20(state_num + 1, move3(num)) and \
               game20(state_num + 1, move4(num))


def game21(state_num, num):
    if (state_num == 1 or state_num == 3) and win(num):
        return False
    elif state_num == 2 and win(num):
        return True
    elif state_num == 4:
        return win(num)
    if state_num % 2 == 0:
        return game21(state_num + 1, move1(num)) and \
               game21(state_num + 1, move2(num)) and \
               game21(state_num + 1, move3(num)) and \
               game21(state_num + 1, move4(num))
    else:
        return game21(state_num + 1, move1(num)) or \
               game21(state_num + 1, move2(num)) or \
               game21(state_num + 1, move3(num)) or \
               game21(state_num + 1, move4(num))


print("20:")
for i in range(1, 94):
    if game20(0, [13, i]):
        print(i)


print("\n21:")
for i in range(1, 94):
    if game21(0, [13, i]):
        print(i)
