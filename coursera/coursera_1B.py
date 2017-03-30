num = 49
tens = num // 10
print tens     #4

num = 49
tens = num // 10
ones = num %  10
print tens,ones     #4 9
print 10 * tens + ones #49

num = 72
tens = num / 10
print tens     #7

a = 2
b = -5
c = 800
print (a + b) % c   # -3 % 800 = 797

a = 10
b =  4
c = 800
print (a + b) % c   # 14 % 800 = 14

hour = 3
ones = hour % 10
tens = hour / 10
print tens, ones, ":00"             #0 3 :00
print str(tens), str(ones), ":00"   #0 3 :00
print str(tens) + str(ones) + ":00"   #03:00

a = 7 > 3
print a   #True

x = 5
y = 5
b = x >= y
c = x > y
print b    #True
print c    #False

d = "hello" == 'hello'
# 单等号是赋值，双等号是比较
print d   #True

print (a and b) or (c and (not d))   #True

x = 3
print x == 3  #True

