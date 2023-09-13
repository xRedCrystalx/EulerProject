num = 1

while True:
    for x in range(1,21):
        if num % x != 0:
            break
        elif x == 20 and num % x == 0:
            print(num)
            break
    num += 1
            