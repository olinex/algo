#!/usr/bin/env python3
#-*- coding:utf-8 -*-

'''
@author:    olinex
@time:      2017/7/9 下午3:19
'''

def insert_sort(input_list):
    print('原始牌堆顺序:',input_list)
    for insert_key in range(1,len(input_list)):
        print('第{}次插入:'.format(insert_key))
        print('\t','手牌:',input_list[:insert_key])
        insert_value = input_list[insert_key]
        print('\t','插入牌:',insert_value)
        print('\t','牌堆:',input_list[insert_key + 1:])
        check_key = insert_key - 1
        while check_key >= 0 and input_list[check_key] > insert_value:
            input_list[check_key + 1] = input_list[check_key]
            check_key -= 1
        input_list[check_key + 1] = insert_value
    return input_list

if __name__ == '__main__':
    from random import randint
    insert_sort([randint(1,100) for i in range(10)])