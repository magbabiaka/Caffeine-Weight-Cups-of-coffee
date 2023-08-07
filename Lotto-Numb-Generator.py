# Lottery Numbers generator for Powerball & Megagmillons
# Author: Adebayo Agbabiaka
# Date: 08/7/2023


import random

my_seed_list = list(range(1, 1001))

def lotteryFunc(n, b, seed):
    random.seed(seed)
    list_num = random.sample(range(1, n + 1), 5)
    ball = random.randint(1, b)
    return list_num, ball

while True:
    print("Enter the single alphabet in CAPS:")
    lottery_type = input("Powerball- 'P' // Megamillions - 'M' // Exit - 'E' :\n")
    seed = random.choice(my_seed_list)

    if lottery_type == 'P':
        nums, ball = lotteryFunc(70, 27, seed)
        print(f"Powerball Numbers - Quick Pick: {nums} - {ball}\n\n")

    elif lottery_type == 'M':
        nums, ball = lotteryFunc(71, 26, seed)
        print(f"Megamillions Numbers - Quick Pick: {nums} - {ball}\n\n")

    elif lottery_type == 'E':
        print("\nThanks for using the lottery random number generator program")
        break

    else:
        print("\nTry again !!! Please enter a proper input alphabet:")
        print("=================================================\n")
