#! /usr/bin/env python
# -*- coding: utf-8 -*-
# describe : 基础语法

# 如何定义一个变量
value_name = "gl"

# 如何确定这个变量的数据类型
print(type(value_name))

# 如何定义一个 char
# char_value = char('f')
# print(type(char_value))


# 如何定义一个 list , set
list_value = []
print(type(list_value))

set_value = set()
print(type(set_value))

dict_value = {}
print(type(dict_value))

# 循环数组
list_a = [1, 2, 3, 4, 5]

for item in list_a:
    print(item)

# dict 循环
dic = {
    "a": "第一个字母"
}

for item in dic:
    print(item, dic[item])

# 分支语句 if
a = 16
b = 15
if a > b:
    print("a>b")
else:
    print("a < b")


# 函数定义
def function_name(args: 'str') :
    print(args)
    return 0.1


if __name__ == '__main__':
    f = function_name(1)

    print(f)
    print(type(f))
