# words="Hai I'm Aswinkumar and Im from Nagercoil"
# word=""
# length=0
# for i in words:
#     if i!=" ":
#         word=word+i
#         if len(word)>length:
#             length=len(word)
#             longest=word
#     else:
#         word=""
# print(longest,"is the longest word.")
    

# words="Hai I'm Aswinkumar and Im from nagercoil "
# list=[]
# longest=""
# length=0

# for i in words:
#     if i!=" ":
#         longest=longest+i
#         # list=list+[longest]
#     else:
#         list=list+[longest]
#         longest=""
# print(list)
# for j in list:
#     word=len(j)
#     if word>length:
#         length=word
#         longest=j
# print(longest,"is the longest word.")

# num=[2,3,5,4,7,9,8,6]
# sum=9
# list=[]
# for i in range(len(num)):
#     for j in range(i+1,len(num)):
#         if num[i]+num[j]==sum:
#             list=list+[(num[i],num[j])]
# print(list)

words="Hai Im aswin and Im from nagercoil"
list=words.split()
word=""
vow_len=0
vowels=['a','e','i','o','u']

# for i in words:
#     if i.isalpha():
#         word=word+i
#     else:
#         list=list+[word]
#         word=""
print(list)
vow_word=""
for j in list:
    count=0
    for k in j:
        if k.lower() in vowels:
            count=count+1
    if count>vow_len:
        vow_len=count
        vow_word=j
print("Maximum vowels word :",vow_word)