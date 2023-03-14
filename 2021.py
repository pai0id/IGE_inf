def move1(num):
    return num+1
def move2(num):
    return (num*3)-2
def win(num):
    return num >= 31
def game20(state_num, num):
    if state_num < 3 and win(num):
        return False
    elif state_num == 3:
        return win(num)
    if state_num % 2 == 0:
        return game20(state_num + 1, move1(num)) or \
               game20(state_num + 1, move2(num))
    else:
        return game20(state_num + 1, move1(num)) and \
               game20(state_num + 1, move2(num))
def game21(state_num, num):
    if (state_num == 1 or state_num == 3) and win(num):
        return False
    elif state_num == 2 and win(num):
        return True
    elif state_num == 4:
        return win(num)
    if state_num % 2 == 0:
        return game21(state_num + 1, move1(num)) and \
               game21(state_num + 1, move2(num))
    else:
        return game21(state_num + 1, move1(num)) or \
               game21(state_num + 1, move2(num))


print("20:")
for i in range(2,31):
    if game20(0, i):
        print(i)


print("\n21:")
for i in range(2,31):
    if game21(0, i):
        print(i)
