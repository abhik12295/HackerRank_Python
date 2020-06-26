import sys


class Solution:
    def __init__(self):
        self.stack=list()
        self.queue=list()
        return None

    def pushCharacter(self,char):
        return self.stack.append(char)


    def enqueueCharacter(self,char):
        return self.queue.append(char)

    def popCharacter(self):
        return self.stack.pop(-1)   #remove from above that is last element

    def dequeueCharacter(self):
        return self.queue.pop(0)    #remove starting from first element



# Write your code here


# read the string s
s = input().lower()
# Create the Solution class object
obj = Solution()

l = len(s)
# push/enqueue all the characters of string s to stack
for i in range(l):
    obj.pushCharacter(s[i])
    obj.enqueueCharacter(s[i])

isPalindrome = True
'''
pop the top character from stack
dequeue the first character from queue
compare both the characters
'''
for i in range(l // 2):
    if obj.popCharacter() != obj.dequeueCharacter():
        isPalindrome = False
        break
# finally print whether string s is palindrome or not.
if isPalindrome:
    print("The word, " + s + ", is a palindrome.")
else:
    print("The word, " + s + ", is not a palindrome.")