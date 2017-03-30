# computer the area of a triangle 三角形面积
# 函数
def triangle_area(base,height):       #函数头define,参数,冒号(很重要)
    area = (1.0 / 2) * base * height    #上句冒号后面下是语句块,语句块要缩进
    return area                       
a1 = triangle_area(3,8)                #调用函数
print a1
a2 = triangle_area(6,9)
print a2

# converts fahrenhait to celsius  华氏度转化为摄氏度
def fahrenheit_to_celsius(fahrenheit):
    celsius = (5.0 / 9) * (fahrenheit - 32)
    return celsius
# test! 测试
c1 = fahrenheit_to_celsius(32)
c2 = fahrenheit_to_celsius(212)
print c1,c2

# converts fahrenhait to kelvin  华氏度转化为开尔文
def fahrenheit_to_kelvin(fahrenheit):
    celsius = fahrenheit_to_celsius(fahrenheit)
    kelvin = celsius + 273.15
    return kelvin
# test!
k1 = fahrenheit_to_kelvin(32)
k2 = fahrenheit_to_kelvin(212)
print k1,k2

# prints hello,world!
def hello():
    print "Hello, world!"
    #hello()  #注释去掉后会无限循环打印hello，world
    return None    #如果并不需要写，系统自动补充，但是不要忘记return
# test!
hello() # 无参数，不返回任何值

h = hello() #赋值给变量，返回None
print h
