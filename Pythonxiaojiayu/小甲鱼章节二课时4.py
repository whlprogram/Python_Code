import random
secret = random.randint(1,10)
print('.............我爱鱼工作室................')
temp = input ('不妨猜一下小甲鱼心里想的是哪个数字：')
guess = int (temp)
while guess != 8:
    temp = input ('哎呀，输错了，请重新输入吧：')
    guess = int (temp)
    if guess == secret:
        print("哇草，你是小甲鱼心中的蛔虫吗？")
        print("哼，猜中了也没有奖励")
    else:
        if guess > secret:
            print ("哥，大了大了！")
        else:
            print("嘿，小了！小了！")
print("游戏结束，不玩啦！")
    
