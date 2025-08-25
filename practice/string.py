
# Write a program that counts how many times "is" appears in a sentence.
# s ='This Is nice, it Is fun'
# s=s.casefold()
# print(s)
# sl=s.split()
# cnt = sl.count('it')
# print(cnt)

# index=[]
# cnt=0
# for i,v in enumerate(sl):
#     if v == 'is':
#         cnt+=1
#         index.append(i)

# print(cnt)
# print(index)

# s ='This Is nice, it Is fun'
# rev=s[::-1]
# print(rev)
# rev=""
# rev="".join(reversed(s))

# for ch in s:
#     print(ch)
#     rev = ch + rev

# print(rev)
# s = s.split()

# s=list(s)
# rev=''.join(reversed(s))

# print(rev)
# i =len(s)-1
# lst=''
# while i >= 0:
#    print(s[i]) 

#    i-=1

# 1.Count vowels manually

# vowels='a,e,i,o,u'
# cnt=0
# s=s.casefold()
# for i in s:
#     # print(i)
#     if i in vowels:
#         cnt+=1
# print(cnt)
# --------------------------------------
#2. Check palindrome

# using slicing
# s='madam'
# n=len(s)
# if s==s[::-1]:
#         print(True)
# else:
#         print(False)

# without slicing
# is_palindrome = True

# for i in range(n//2):
#     if s[i] != s[n-i-1]:
#         is_palindrome=False
#         break

# print(is_palindrome)
# ----------------------------------------

# Find first non-repeating character
# 👉 Input: "aabbcde" → Output: c
# -----------------------------------------

# --------------------------------

# Remove duplicate characters
# 👉 Input: "programming" → Output: "progamin"
    
# s="programming"

# res=''

# for i in s:
#     if i not in res:
#         res+=i

# print(res)

# -----------------------

""" Find longest word in a sentence 👉 
Input: "I love python programming" → Output: "programming" """
# ------------------------------------

# s="I love python programming"

# s=s.split()
# l=""

# for i in s:
#     if len(i)>len(l):
#         l=i

# print(l)

# --------------------------------------------------
'''Reverse a string manually
👉 Input: "hello" → Output: "olleh"
(Hint: build a new string character by character from the end)'''

# s="hello"
# rev=""

# for i in range(len(s)-1,-1,-1):
#     rev+=s[i]


# print(rev)
# ----------------------------------------------
"""Count consonants in a string
👉 Input: "hello world" → Output: 7"""

# s="hello world"

# vowels=['a','e','i','o','u']
# cnt=0
# for i in s:
#     if i not in vowels and i != ' ':
#         cnt+=1


# print(cnt)

# -------------------------------------
"""
Find the most frequent character
👉 Input: "success" → Output: "s"
(Hint: keep a dictionary or manual counting)
"""
# s="success"

# f={}

# for i in s:
#     if i in f:
#         f[i]+=1
#     else:
#         f[i]=1

# max_char= None
# max_count= 0

# for i in f:
#     if f[i] > max_count:
#         max_count = f[i]
#         max_char = i

# print(max_char)

# max_char=""
# max_cnt=0

# for i in s:
#     cnt=0
#     for j in s:
#         if i == j:
#             cnt+=1
#     if cnt > max_cnt:
#             max_cnt= cnt
#             max_char = i

# print(max_char)


# mx_chr=""
# mx_cnt=0

# for i in s:
#     cnt=0
#     for j in s:
#         if i == j:
#             cnt+=1
#     if cnt > mx_cnt:
#         mx_cnt = cnt
#         mx_chr = i


# print(mx_chr)


x = '121'
is_palindrome=True
for i in range(len(x)//2):
    if x[1::] == x[::-1]:
        is_palindrome=False
        break
            
print(is_palindrome)