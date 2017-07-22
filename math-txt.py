# -*- coding:utf-8 -*-

__author__ = 'zhengbiqing 460356155@qq.com'
__doc__ = """武汉市光谷一小二年级数学口算自动出题程序 2017-05-31"""

from random import randint

sym = [' + ', ' - ']

# 当前文件夹下创建口算题目文件math.txt
fobj = open('math.txt', 'w')


def function_oneline(pmin, pmax, mmin, mmax, multimin, multimax, divmin, divmax):
    '''
    pmin,pmax:加数、被加数最小最大值
    mmin,mmax:减法转换成加法后，加数、被加数最小最大值
    multimin,multimax:乘数、被乘数最小最大值
    divmin,divmax:除法转换成乘法后，乘数、被乘数最小最大值
    '''

    # plus：加法算式，rjust(2)：按2位数右对齐
    plus = str(randint(pmin, pmax)).rjust(2) + ' + ' + str(randint(pmin, pmax)).rjust(2) + ' ='

    # minus：减法算式
    minus1 = randint(mmin, mmax)
    minus2 = randint(mmin, mmax)
    minussum = minus1 + minus2
    minus = str(minussum).rjust(2) + ' - ' + str(minus1).rjust(2) + ' ='

    # multi：乘法算式
    multi1 = randint(multimin, multimax)
    multi2 = randint(multimin, multimax)
    multi = str(multi1).rjust(2) + ' x ' + str(multi2).rjust(2) + ' ='

    # div：除法算式
    div1 = randint(divmin, divmax)
    div2 = randint(divmin, divmax)
    divmulti = div1 * div2
    div = str(divmulti).rjust(2) + ' /' + str(div1).rjust(2) + ' ='

    lineitem = [plus, minus, multi, div]
    line = '                  '.join(lineitem)
    print line
    fobj.writelines(line + '\r\n')


# 4列x10行道加、减、乘、除基本题，每行加、减、乘、除题各1道
def function():
    for col in range(10):
        function_oneline(1, 20, 1, 50, 1, 9, 1, 9)


# 类型1算式：... +/- ... +/- ...
def func1(summin=1, summax=100):
    '''
    summin,summax:允许总和的最小最大值
    '''
    sym1 = sym[randint(0, 1)]
    sym2 = sym[randint(0, 1)]
    first = 0
    second = 0
    third = 0

    if sym1 == ' + ' and sym2 == ' + ':
        sum_ = randint(summin + 2, summax)
        first = randint(summin, sum_ - 2)
        second = sum_ - first
        second = randint(summin, second - 1)
        third = sum_ - first - second
    elif sym1 == ' + ' and sym2 == ' - ':
        sum_ = randint(summin + 1, summax)
        first = randint(summin, sum_ - 1)
        second = sum_ - first
        third = randint(summin, sum_)
    elif sym1 == ' - ' and sym2 == ' + ':
        first = randint(summin + 1, summax)
        second = randint(summin, first)
        third = randint(first - second, summax)
    elif sym1 == ' - ' and sym2 == ' - ':
        first = randint(summin + 2, summax)
        second = randint(summin, first)
        third = first - second
        third = randint(summin, third)

    athstr = str(first).rjust(2) + sym1 + str(second).rjust(2) + sym2 + str(third).rjust(2)
    print athstr
    return athstr


# 类型2算式：... +/- ... x ...
def func2(multimin=1, multimax=9, summin=1, summax=100):
    '''
    multimin,multimax:乘数、被乘数最小最大值
    summin,summax:允许总和的最小最大值
    '''
    sym1 = sym[randint(0, 1)]
    first = 0
    second = 0
    third = 0

    if sym1 == ' + ':
        second = randint(multimin, multimax)
        third = randint(multimin, multimax)
        first = randint(summin, summax - second * third)
    else:
        second = randint(multimin, multimax)
        third = randint(multimin, multimax)
        first = randint(second * third, summax)

    athstr = str(first).rjust(2) + sym1 + str(second).rjust(2) + ' x ' + str(third).rjust(2)
    print athstr
    return athstr


# 类型3算式：(... +/- ...) / ...
def func3(multimin=1, multimax=9, summin=1, summax=100):
    '''
    multimin,multimax:乘数、被乘数最小最大值
    summin,summax:允许总和的最小最大值
    '''
    sym1 = sym[randint(0, 1)]
    first = 0
    second = 0
    third = 0

    if sym1 == ' + ':
        second = randint(multimin, multimax)
        third = randint(multimin, multimax)
        first = randint(summin, second * third)
        second = second * third - first
    else:
        second = randint(multimin, multimax)
        third = randint(multimin, multimax)
        multi = second * third
        second = randint(summin, summax - multi)
        first = multi + second

    athstr = '(' + str(first).rjust(2) + sym1 + str(second).rjust(2) + ')' + ' / ' + str(third).rjust(2)
    print athstr
    return athstr


# 基本题
function()
# 类型1题
plus1 = func1()
plus2 = func1()
# 类型2题
plus3 = func2()
# 类型3题
plus4 = func3()
plus5 = func3()

# 类型1、2题打印一行
line = [plus1, plus2, plus3]
lines = '                             '.join(line)
print lines
fobj.writelines(lines + '\r\n\r\n\r\n\r\n')

# 类型3题打印一行
line = [plus4, plus5]
lines = '                             '.join(line)
print lines
fobj.writelines(lines)
fobj.writelines('\r\n\r\n\r\n\r\n')
fobj.writelines(r'用时______分钟           对______题（共45题）           家长签名：')


# 一张A4纸上下各打印1分
fobj.writelines('\r\n\r\n\r\n\r\n')
fobj.writelines('\r\n\r\n')


# 基本题
function()
# 类型1题
plus1 = func1()
plus2 = func1()
# 类型2题
plus3 = func2()
# 类型3题
plus4 = func3()
plus5 = func3()

# 类型1、2题打印一行
line = [plus1, plus2, plus3]
lines = '                             '.join(line)
print lines
fobj.writelines(lines + '\r\n\r\n\r\n\r\n')

# 类型3题打印一行
line = [plus4, plus5]
lines = '                             '.join(line)
print lines
fobj.writelines(lines)
fobj.writelines('\r\n\r\n\r\n\r\n')
fobj.writelines(r'用时______分钟           对______题（共45题）           家长签名：')

fobj.close()
