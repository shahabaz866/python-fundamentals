
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
s='madam'
n=len(s)
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

s="hello"
rev=""

for i in range(len(s)-1,-1,-1):
    rev+=s[i]


print(rev)

