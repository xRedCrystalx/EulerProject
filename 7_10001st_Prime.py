num: int = 7
loop: bool = True
counter: int = 4

while loop:
    for i in range(num // 2, 1, -1):
        if num % i == 0 and i != 1:
            break
        elif i == 1:
            if counter+1 == 10001:
                print(num)
                loop = False
            else:
                counter += 1
                print(counter)
        else:
            print(i)
    num += 1
    print(num)