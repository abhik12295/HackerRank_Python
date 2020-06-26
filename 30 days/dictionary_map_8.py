# The first line contains an integer, n, denoting the number of entries in the phone book.
# Each of the  subsequent lines describes an entry in the form of 2 space-separated values on a single line.
# The first value is a friend's name, and the second value is an 8-digit phone number.
# After the  n lines of phone book entries, there are an unknown number of lines of queries.
# Each line (query) contains a  name to look up, and you must continue reading lines until there is no more input.
# Note: Names consist of lowercase English alphabetic letters and are first names only

import sys
n=int(input())
contact=dict()
for i in range(n):
    # d=dict(input().split() for _ in range(n))
    # print(d)
    x=input().split(" ")
    contact[x[0].lower()]=int(x[1])
print(contact)
# a_keys=list(contact.keys())
# print(a_keys)
# a_values=list(contact.values())
# t=0
# for z in range(n):
#     y=input().lower()
#     if y in a_keys:
#         print('{}={}'.format(y,a_values[t]))
#     else:
#         print("Not found")
#     t=t+1

for z in range(n):
    y=input().lower()
    if y in contact:
        print('{}={}'.format(y,str(contact[y])))
    else:
         print("Not found")

# lines=sys.stdin.readlines()
# for z in lines:
#     y=z.strip()
#     if y in contact:
#         print("{}={}".format(y,str(contact[y])))
#     else:
#         print("Not found")