#1.
# import math
# a = float(input('a='))
# b = float(input('b='))
# c = float(input('c='))
# if 0 < (b ** 2 - 4 * a * c):
#     r1 = (-b + math.sqrt(b ** 2 - 4 * a * c)) / 2 * a
#     r2 = (-b - math.sqrt(b ** 2 - 4 * a * c)) / 2 * a
#     print(r1,r2)
# elif 0 == (b ** 2 - 4 * a * c):
#     r1 = r2 = -b / (2 * a)
#     print(r1)
# else:
#     print('the equation has no real roots')    
#2.
# import numpy as np 
# number1 = int(np.random.uniform(1,100))
# number2 = int(np.random.uniform(1,100))
# print(number1,number2)
# user = int(input('两数之和为：'))
# if user == number1 +number2:
#     print('true')
# else:
#     print('false')
#3.
# a = int(input('请输入数字0-6：'))
# if a > 6:
#     print('false')
# elif a == 0:
#     print('今天是星期日')
# elif a == 1:
#     print('今天是星期一')
# elif a == 2:
#     print('今天是星期二')
# elif a == 3:
#     print('今天是星期三')
# elif a == 4:
#     print('今天是星期四')
# elif a == 5:
#     print('今天是星期五')
# else:
#     print('今天是星期六')
#4.
# a,b,c = map(int,input('输入三个数：').split())
# num_ = [a,b,c]
# num_ .sort()
# print(num_)



#5.
# price1,weight2 = map(float,input('输入第一组价格和重量：').split())
# price2,weight2 = map(float,input('输入第二组价格和重量：').split())
# if price1 > price2:
#     print('第二组价格更好')
# else:
#     print('第一组价格更好')
#6.
# year,month = map(int,input('请输入年和月：').split())
# if month > 12:
#     print('输入有误')
# elif year % 4 == 0 and month == 2:
#     print('%d年%d月有29天'%(year,month))
# elif month == 2:
#     print('%d年%d月有28天'%(year,month))    
# elif month == 1 or month == 3  or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
#     print('%d年%d月有31天'%(year,month))
# else:
#     print('%d年%d月有30天'%(year,month))
#7.
# import numpy as np
# guess = np.random.choice(['正面','反面'])
# user = input('请给出猜想：')
# if user == guess:
#     print('正确')
# else:
#     print('错误')
# print(guess)

#8.
# import numpy as np
# res = np.random.choice(['剪刀','石头','布'])
# print(res)
# 0 == '剪刀'
# 1 == '石头'
# 2 == '布'
# user = input('输入数字0表示剪刀，1表示石头，2表示布')
# if res ==user:
#     print('平局')
# elif res == 1 and user == 0:
#     print('你输了')
# elif res == 0 and user == 2:
#     print('你输了')
# elif res == 2 and user == 1:
#     print('你输了')
# else:
#     print('你赢了')




#9.
# year,m,q = map(int,input('请输入一个世纪的某年，月份，天：').split())
# j = year / 100
# k = year % 100
# h = (q + (26 * (m + 1) / 10) + k + (k / 4) + (j / 4) + 5 * j) % 7
# print('今天是星期%d'%h)


#10.
# import numpy as np
# color = np.random.choice(['梅花','红桃','方块','黑桃'])
# number = np.random.choice(['A','2','3','4','5','6','7','8','9','10','Jack','Queen','King'])
# print('你抽取的是%s%s'%(color,number))

#11.
# a = input('请输入一个数：')
# a1 = a[::-1]
# if a1 == a:
#     print('%s是回文数'%a)
# else:
#     print('%s不是回文数'%a)


#12.
# a,b,c = map(int,input('输入三角形的三个边长：').split())
# n = [a,b,c]
# n.sort()
# if n[2] < (n[0] + n[1]):
#     print(a + b + c)
# else:
#     print('输入非法')

#13.











