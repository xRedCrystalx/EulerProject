biggest_palindrome: int = 0

for first_num in range(1000):
    for second_num in range(1000):
        product: int = first_num * second_num
        if str(product) == str(product)[::-1]:
            if product > biggest_palindrome:
                biggest_palindrome = product
                
print(biggest_palindrome)