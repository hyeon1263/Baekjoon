# -*- coding: utf-8 -*-
"""백준2331

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1HN_gRy43AldNa9saxkLXwYcLiWEkTGN2
"""

# 반복수열

A, P = map(int, input().split())

seq = [A]
while 1:
    sum = 0
    for i in str(A):
        sum += int(i)**P
    A = sum
    if A in seq:
        seq = seq[:seq.index(A)]
        break
    else:
        seq.append(A)
print(len(seq))