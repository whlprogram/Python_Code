bingo = '王海龙是帅哥'
answer = input('请输入王海龙最想听的一句话：')

while True:
    if answer == bingo:
        break
    answer = input('抱歉，错了，请重新输入(答案正确才能退出游戏):')

print ('说得好')
