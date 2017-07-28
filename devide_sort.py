#!/usr/bin/env python3
#-*- coding:utf-8 -*-

'''
@author:    olinex
@time:      2017/7/28 下午12:58
'''

def merge(input_list,left_start,middle,right_end):
    sort_list = []
    left = left_start
    right = middle
    while left <= middle-1 and right <= right_end - 1:
        left_value = input_list[left]
        right_value = input_list[right]
        if left_value < right_value:
            sort_list.append(left_value)
            left += 1
        else:
            sort_list.append(right_value)
            right += 1
    else:
        if left == middle:
            sort_list = sort_list + input_list[right:right_end]
        else:
            sort_list = sort_list + input_list[left:middle]
    for value in sort_list:
        input_list[left_start] = value
        left_start += 1
    del sort_list

def devide_sort(input_list,start=None,end=None):
    start = start or 0
    end = end or len(input_list)
    middle = (end + start) // 2
    if (end - start) > 1:
        devide_sort(input_list,start,middle)
        devide_sort(input_list,middle,end)
    print(input_list)
    merge(input_list,start,middle,end)


if __name__ == '__main__':
    from random import randint
    a=[randint(0,1000) for i in range(0,10)]
    # a=[2,3,6,5]
    print('init',a)
    devide_sort(a)
    print('end',a)
