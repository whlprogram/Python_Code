def volume_cube(side):
    return side ** 3

s = 2
print "Volume of cube with side", s, "is", volume_cube(s), "."
# Volume of cube with side 2 is 8 .  2��3�η���8


import random
def random_dice():
    die1 = random.randrange(1,7)
    die2 = random.randrange(1,7)
    return die1 + die2
#��������ӣ��������������ĺ�
print "Sum of two random dice,rolled once:",random_dice()
print "Sum of two random dice,rolled again:",random_dice()

print 10 - - 2  #�൱��print 10 - (-2)
