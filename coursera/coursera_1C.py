def greet(friend, money):
    if friend and (money > 20): #friendĬ��ΪTrue
        print "Hi!"
        money = money - 20
    return money

money = 25

#�򵥵��ú���
m = greet(True, money)  #Hi!   (��������)
print "Money:", m       #Money: 5 
print ""       
m = greet(False, money)  #������������������
print "Money:", m        #Money: 25 
print ""

#�������ú���,����ֵ
money = greet(True, money)   #Hi!   (��������)
print "Money:", money        #Money: 5
print ""                     #�Ѿ���5��ֵ��money
money = greet(False, money)  #������������������
print "Money:", money        #Money: 5 
print ""
money = greet(False, money)  #������������������
print "Money:", money        #Money: 5
print ""



def greet(friend, money):
    if friend and (money > 20): #friendĬ��ΪTrue
        print "Hi!"
        money = money - 20
    elif friend:
        print "Hello!"
    else:
        print "Ha ha"
        money = money + 20         
    return money

#�ж��Ƿ�Ϊ����
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

