print 3,-1,3.14159,-2   #3 -1 3.14159 -2

print type(3)          # <type 'int'>
print type(-2)         # <type 'int'>
print type(3.14159)    # <type 'float'>
print type(3.0)        # <type 'float'>
print type(3.14159),type(3.0) #<type 'float'> <type 'float'>

print int(-1)           # -1
print int(3.14159)      # 3
print float(-2)         # -2.0
print float(3)          # 3.0

print int(3.14159),float(-2) # 3  -2.0

print float (3);        # 3.0

print 3.141593467823468763547  # 3.14159346782
print 1.2323424232323          # 1.23234242323
print 3.14159346782945         # 3.14159346783

print 1 + 2, 3 - 8, 5 * 5, 4 ** 2 # 3 -5 25 16

print 7.0 / 5, 3.3 / 3.3, 7 / 5.0 # 1.4 1.0 1.4
print 6 / 2, 7 / 3, 8 / 5         # 3 2 1
print -9 / 4                      # -3
print -9 / 3                      # -3
print 5 / 2                       # 2
print -5 / 2                      # -3
print -10 / 3                     # -4 

print 1 + 2 * 3, 4.0 - 5.0 /6.0, 7 * 8 + 9 * 10 # 7 3.16666666667 146

# 运算优先级 **      * , /      + , -
print 6 / 2 + 2 ** 2  #先运算**（2的2次方），再运算除法，最后运算+
print 5 / 2 * 3       #运算优先级*和/一样，+和- 一样
print 3 - 2 + 7


