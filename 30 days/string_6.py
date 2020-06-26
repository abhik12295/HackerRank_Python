n= int(input())
for i in range(n):
    s=input()
    # x=len(s)
    print("{} {}".format(s[0:len(s):2],s[1:len(s):2]))