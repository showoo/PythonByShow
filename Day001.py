#1.
# temperature = float(input('输入一个摄氏温度：'))
# fahrenheit = 1.8 * temperature + 32
# print('%.2f转化为华氏温度为：%.2f'%(temperature,fahrenheit) )


#2.
# import math
# radius,height = map(float,input('输入输入底面圆的半径和圆柱的高：').split())
# area = float(radius * radius * math.pi)
# volume = area * height
# print('圆柱的体积是：%.2f'%volume)


#3.
# foot = float(input('输入英尺数：'))
# meters = 0.305 * foot
# print('%f转化后为%f米'%(foot,meters)) 


#4.
# water_kg = float(input('输入水的质量单位kg：'))
# initialTemperature = float(input('输入水的初始温度单位C：'))
# finalTemperature = float (input('输入水的最终温度单位C：'))
# energy = water_kg * (finalTemperature - initialTemperature) *4184
# print('水从初始温度到达最终温度需要的能量为：%fJ'%energy)


#5.
# difference,rate = map(float,input('输入差额和年利率').split())
# interest = difference *(rate / 1200)
# print('下月要付的利息为：%f'%interest)


#6.
# v0,v1,time = map(float,input('输入初速度，末速度，以秒为单位的变化所占时间').split())
# acceleration = (v1 - v0) / time
# print('平均加速度为;%f'%acceleration)


#7.
# deposit = float(input('输入存款数：'))
# balance == 0
# for balance = balance + 1 ：
# balance = (deposit + balance） * (1 + 0.05 / 12)


# 8.
# number = int(input('输入一个整数：'))
# ge = int(number % 10)
# shi = int((number // 10) % 10)
# bai = int((number // 100) % 10)
# sum = ge + shi + bai
# print('the sum of the digits is %i'%sum)


#9.
# import math
# radius = float(input('输入五边形的半径：'))
# side = 2 * radius * math.sin(math.pi / 5)
# area = 5 * side * side / (4 * math.tan(math.pi / 5))
# print('五边形的面积是：%f'%area)


#10.
# import math
# jingdu1,weidu1 = (float,input('请输入点1经度和纬度：').split())
# jingdu2,weidu2 = (float,input('请输入点2经度和纬度：').split())
# d = float(float(6371.01) *  math.acos(math.sin(math.radians(jingdu1)) * math.sin(math.radians(jingdu2)) + math.cos(math.radians(jingdu1)) * math.cos(math.radians(jingdu2)) * math.cos((weidu1 - weidu2))))
# print('大圆距离是：%f'%d)


#a = int(input('输入：'))
#b = int(input('输入：'))
#print (a - b)
#print('%.2f - %.2f =%.2f'%(a,b,a - b))
#print('{} - {} = {}'.format(a,b,a - b))

#a = 'joker is a good man'
# a = 'b'
# print(ord(a))
#print(chr(a))

# email = '666@qq.com'
# for e in email:
#     o = ord(e)
# print(o)

# import hashlib
# m = hashlib.md5()
# a = input('输入：')
# m.update(bytes(a,encoding = 'utf8'))
# print(m.hexdigest())

# a= 'joker is a good man'
# print(a[-1])        #=length-1
# print(a[0:5:2])       #[start:end：step) 切片是一个前闭后开的区间
# print(a[::-1])   #反转

# a = 100
# b = 100
# print(a != b)         #<= >= 类型不同不能比
# rint(a is b)         #is 判断的是内存地址
# print(id(a))                   #查看内存地址

# a = 'joker is a good man'
# print('j' in a) #in 判断在容器中(可迭代对象)有没有这个对象
# print('ok' not in a )

# print(False and True)

# a = 10
# a += 10 #a = a + 10

# year = int(input('输入年份：'))
# if (year % 100 !=0 and year % 4 == 0) or year %400 ==0:
#     print('%d 是闰年'%year)
# else:
#     print('%d 不是闰年'%year)

# a = float(input('输入一个华氏温度：'))
# b =  (a - 32) / 1.8
# print('%.2f' %b)

# number = input('输入一个数：')
# bai = int(number[0])
# shi = int(number[1])
# ge = int(number[2])
# if bai **3 + shi **3 + ge **3 == int(number):
#     print('是水仙花数')
# else:
#     print('不是水仙花数')