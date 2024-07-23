#recursion
# def poly(s):
#     if len(s) <= 1:
#         return True
#     elif s[0] != s[-1]:
#         return False
#     return poly(s[1:-1])
#
#
# if __name__ == "__main__":
#     n = input("enter name: ")
#     if poly(n):
#         print("This is polindrome")
#     else:
#         print("This is not polindrome")

#Using loop

def poly(s):
    length=len(s)
    for i in range (length // 2):
        if(s[i]!=s[length-i-1]):
            return False
    return True
if __name__=="__main__":
    n=input("Enter Char: ")
    if poly(n):
        print("This is polindrome")
    else:
        print("This is not polidrome")

