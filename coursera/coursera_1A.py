# computer the area of a triangle ���������
# ����
def triangle_area(base,height):       #����ͷdefine,����,ð��(����Ҫ)
    area = (1.0 / 2) * base * height    #�Ͼ�ð�ź�����������,����Ҫ����
    return area                       
a1 = triangle_area(3,8)                #���ú���
print a1
a2 = triangle_area(6,9)
print a2

# converts fahrenhait to celsius  ���϶�ת��Ϊ���϶�
def fahrenheit_to_celsius(fahrenheit):
    celsius = (5.0 / 9) * (fahrenheit - 32)
    return celsius
# test! ����
c1 = fahrenheit_to_celsius(32)
c2 = fahrenheit_to_celsius(212)
print c1,c2

# converts fahrenhait to kelvin  ���϶�ת��Ϊ������
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
    #hello()  #ע��ȥ���������ѭ����ӡhello��world
    return None    #���������Ҫд��ϵͳ�Զ����䣬���ǲ�Ҫ����return
# test!
hello() # �޲������������κ�ֵ

h = hello() #��ֵ������������None
print h
