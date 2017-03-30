def volume_cube(side):
    return side ** 3

s = 2
print "Volume of cube with side", s, "is", volume_cube(s), "."
# Volume of cube with side 2 is 8 .  2的3次方是8


import random
def random_dice():
    die1 = random.randrange(1,7)
    die2 = random.randrange(1,7)
    return die1 + die2
#随机掷骰子，掷两次所得数的和
print "Sum of two random dice,rolled once:",random_dice()
print "Sum of two random dice,rolled again:",random_dice()

print 10 - - 2  #相当于print 10 - (-2)
