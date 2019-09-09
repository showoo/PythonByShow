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

number = int(input('输入一个数：'))
bai = int(number[0])
shi = int(number[1])
ge = int(number[2])
if bai **3 + shi **3 + ge **3 == int(number):
    print('shi')
else:
    print('bushi')
