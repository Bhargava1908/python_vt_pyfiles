# Random Module
# Used for Random Number Generation
import random


random_number = random.random() # Gaussian Distribution
print(random_number)

random_number = random.randint(1, 90)
print(random_number)

l = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
random_element = random.choices(l)
print(random_element)

random_4_elements = random.choices(l, k=4)
print(random_4_elements)

random_number = random.randrange(10, 20, 2)
print(random_number)

l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
random.shuffle(l)
print(l)

l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
random_number = random.choice(l)
print(random_number)

random_numbers = random.sample(l, k=4)
print(random_numbers)

random.seed(1)
random_number = random.randint(1, 10)
print(random_number)
random.seed(1)
random_number = random.randint(1, 10)
print(random_number)
