def find_max(numbers):
    maximum = numbers[0]
    for num in numbers:
        if num>maximum:
            maximum=num
    return maximum


import random
class Dice():
    def roll(self):
        first=random.randint(1,6)
        second=random.randint(1,6)
        return first,second


