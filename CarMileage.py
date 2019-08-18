#https://www.codewars.com/kata/52c4dd683bfd3b434c000292/train/python
import numpy
import pandas
def is_interesting(num, awesome_phrases):
    if len(str(num)) < 3:
        return 0
    l = [num+1,num+2,num-1,num-2]
    if trailingZero(num) == True:
        return 2
    if allSameNums(num) == True:
        return 2
    if sequential(num) == True:
        return 2
    if pal(num) == True:
        return 2
    if num in awesome_phrases:
        return 2
    for i in l:
        if trailingZero(i) == True:
            return 1
    for i in l:
        if allSameNums(i) == True:
            return 1
    for i in l:
        if sequential(i) == True:
            return 1
    for i in l:
        if pal(i) == True:
            return 1
    for i in l:
        if i in awesome_phrases:
            return 1
    else:
        return 0

def trailingZero(num):
    s = str(num)
    if len(s) < 2:
        return False
    if int(s[1:]) == 0:
        print('Interesting number based on trailing zeros')
        return True

def allSameNums(num):
    s = str(num)
    if len(''.join(set(s))) < 2:
        print('AllSameNums')
        return True

def sequential(num):
    down = True
    up = True
    s = str(num)
    for i in range(0,len(s)-1):
        if int(s[i]) != (int(s[i+1]) + 1):
            up = False
        if int(s[i]) != (int(s[i+1]) - 1):
            down = False
    if up or down == True:
        print('Sequential')
        return True

def pal(num):
    s = str(num)
    backwards = ''
    for i in range(len(s)-1,-1,-1):
        backwards += s[i]
    if s == backwards:
        print('Palindrome')
        return True
