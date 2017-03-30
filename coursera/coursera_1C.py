def greet(friend, money):
    if friend and (money > 20): #friend默认为True
        print "Hi!"
        money = money - 20
    return money

money = 25

#简单调用函数
m = greet(True, money)  #Hi!   (符合条件)
print "Money:", m       #Money: 5 
print ""       
m = greet(False, money)  #不符合条件，不运行
print "Money:", m        #Money: 25 
print ""

#连续调用函数,并赋值
money = greet(True, money)   #Hi!   (符合条件)
print "Money:", money        #Money: 5
print ""                     #已经将5赋值给money
money = greet(False, money)  #不符合条件，不运行
print "Money:", money        #Money: 5 
print ""
money = greet(False, money)  #不符合条件，不运行
print "Money:", money        #Money: 5
print ""



def greet(friend, money):
    if friend and (money > 20): #friend默认为True
        print "Hi!"
        money = money - 20
    elif friend:
        print "Hello!"
    else:
        print "Ha ha"
        money = money + 20         
    return money

#判断是否为闰年
def is_leap_year(year):
    if (year % 400) == 0:
        return True
    elif ((year % 100) != 0) and ((year % 4) == 0):
        return True
    else:
        return False

year = 2009
leap_year = is_leap_year(year)

if leap_year:
    print year,"is a leap year"
else:
    print year,"is not a leap year"

