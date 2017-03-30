score = int (input('请输入一个分数：'))
if 100 >= score >= 90:
    print ('A')
elif 90  >  score >= 80: # else if
    print ('B')
elif 80  >  score >= 60:
    print ('c')
elif 60  >  score >=  0:
    print ('D')
else : 
    print ('输入错误！')
