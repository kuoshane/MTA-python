import random
num = random.sample(range(1,50),7)
special = num.pop()
num.sort()
print(num)
print("特別數字:" +str(special))
