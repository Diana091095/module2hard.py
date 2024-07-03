import random
def random_number():
    numbers = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    win = random.choice(numbers)
    return win

win = random_number()
print(win)
def check_divisibility(win):
    for i in range(1, 20):
         for k in range(i+1, 20):
             if win % (i + k) == 0:

                 print(f'{i}{k}', end='')
         else:
             continue




check_divisibility(win)






