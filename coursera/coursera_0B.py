print 7 / +4   #1
print 7 / 4    #1
print 7  +4    #11
print +4       #4
print 7 / +6   #1



a = "my_name"    
print a     # my_name "

my_name = " Wang HaiLong "    #空格也会被打印出来
print my_name  # Wang HaiLong 

my_age = 19
print my_age

my_sister_age = my_age + 3.5
print my_sister_age    # 22.5

temp_Fahrenheit = 32  #华氏摄氏度  转换公式 C = 5 / 9 * (F - 32)
temp_Celsius = 5.0 / 9.0 * (temp_Fahrenheit - 32)  #必须用5.0和9.0,因为 5/9=0
print temp_Celsius    #摄氏华氏度 0.0

temp_Fahrenheit = 212  #华氏摄氏度
temp_Celsius = 5.0 / 9.0 * (temp_Fahrenheit - 32)  #必须用5.0和9.0,因为 5/9=0
print temp_Celsius     #摄氏华氏度 100.0

temp_Celsius = 0.0
temp_Fahrenheit = temp_Celsius / (5.0 / 9.0) +32
print temp_Fahrenheit   #华氏摄氏度 32.0
temp_Celsius = 100
temp_Fahrenheit = temp_Celsius * (9.0 / 5.0) +32
print temp_Fahrenheit   #华氏摄氏度 212.0
