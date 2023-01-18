import random

coin = ['heads', 'tails']

side = random.randint(0,1)

result = coin[side].capitalize()

print(result)