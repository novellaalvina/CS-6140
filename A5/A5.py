# Frequent
# -*- coding: utf-8 -*-
"""A5-Frequent.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Xei1cYojq36Lbu0EtoQyq4YjrRd0GpUt
"""

import numpy as np

# s1_load = np.loadtxt('/content/drive/MyDrive/Spring2023/CS4140/S1.txt', dtype = str)
s1 = []
s2 = []
with open('/content/drive/MyDrive/Spring2023/CS4140/S1.txt','r') as file:
  for line in file:
    s1.append(line)
s1 = [*s1[0]]

with open('/content/drive/MyDrive/Spring2023/CS4140/S2.txt','r') as file:
  for line in file:
    s2.append(line)
s2 = [*s2[0]]

k = 12

def MS(S, k):
  C = [0 for i in range(k-1)]
  L = [None for i in range(k-1)]

  for char in S:
    if char in L:
      j = L.index(char)
      C[j] += 1
    else:
      if 0 in C:
        zero_idx = C.index(0)
        L[zero_idx] = char
        C[zero_idx] = 1
      else:
        for id in range(k-1):
          C[id] -= 1
  return C, L

s1_label_count = {}
s2_label_count = {}
s1_label_count_ratio = {}
s2_label_count_ratio = {}

c1, l1 = MS(s1, k)
c2, l2 = MS(s2, k)

c1_ratio = [c/len(s1) for c in c1]
c2_ratio = [c/len(s2) for c in c2]

for i,c in enumerate(c1):
  s1_label_count[l1[i]] = c
for i,c in enumerate(c2):
  s2_label_count[l2[i]] = c

for i,c in enumerate(c1_ratio):
  s1_label_count_ratio[l1[i]] = c
for i,c in enumerate(c2_ratio):
  s2_label_count_ratio[l2[i]] = c

print(s1_label_count)
print(s2_label_count)
print(s1_label_count_ratio)
print(s2_label_count_ratio)

s1_might_must_25 = {}

for char, cr in s1_label_count_ratio.items():
  if cr <= 0.25:
    s1_might_must_25[char] = "might"
  else:
    s1_might_must_25[char] = "must"

s2_might_must_25 = {}

for char, cr in s2_label_count_ratio.items():
  if cr <= 0.25:
    s2_might_must_25[char] = "might"
  else:
    s2_might_must_25[char] = "must"

print(s1_might_must_25)
print(s2_might_must_25)

from IPython.core.compilerop import hashlib
import math
t = 6
k = 12

def count_min_sketch(S, t, k, target):
  C = np.zeros((t, k))
  hashfunctions = ['sha256', 'sha384', 'sha224', 'sha512', 'sha1', 'md5']
  min_char_count = math.inf

  for char in S:

    for j in range(t):
      if j == 0:
        h = int(hashlib.sha384(str(char).encode()).hexdigest(), 16) % k
      elif j == 1:
        h = int(hashlib.sha224(str(char).encode()).hexdigest(), 16) % k
      elif j == 2:
        h = int(hashlib.sha512(str(char).encode()).hexdigest(), 16) % k
      elif j == 3:
        h = int(hashlib.sha1(str(char).encode()).hexdigest(), 16) % k
      elif j == 4:
        h = int(hashlib.sha256(str(char).encode()).hexdigest(), 16) % k
      else:
        h = int(hashlib.sha3_224(str(char).encode()).hexdigest(), 16) % k
      C[j][h] += 1
    if (char == target):
      min_char_count = min(min_char_count, C[j][h])
  return C, min_char_count

char_list = ['a', 'b', 'c']
C_dict = {}
char_count = {}
for char in char_list:
  C, min_char_count = count_min_sketch(s1, t, k, char)
  C_dict[char] = C
  char_count[char] = min_char_count

print(C_dict)
print(char_count)
# {'a': 1.0, 'b': 1.0, 'c': 3.0}
# c 480289 | 0.16009633333333334
# a 899566 | 0.2998553333333333
# b 599564 | 0.19985466666666668
# fq <= fq^ <= fq + 2/k*len(s1)
# fq = 0.25, fq^ = counter
