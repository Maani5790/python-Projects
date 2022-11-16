# num = int(input("enter ur table number"))
# for i in range(1,11):
#     # print(str(num) + "X" + str(i) + "=" + str(i*num))
#     print(f"{num} X {i} = {num*i}")

# li = ["ali", "azlan" , "hammad" , "maani"]
# for name in li : 
#     if name.startswith("a"):
#         print("hello" + name)




# num = int(input("enter ur table number"))
# i = 0
# while i in range(1,11):
#     print(str(num) + "X" + str(i) + "=" + str(i*num))
#     i = i +1
    # print(f"{num} X {i} = {num*i}")




# num = int(input("Enter the number: "))
# prime = True

# for i in range(2, num):
#     if(num%i == 0):
#         prime = False
#         break
# if prime:
#     print("This number is Prime")
# else:
#     print("This number is not Prime")


# num = int(input("Enter the number: "))
# factorial = 1
# for i in range(1, num+1):
#     factorial = factorial * i
# print(f"The factorial of {num} is {factorial}")



# n = 4 
# for i in range(4):
#     print("*"  * (i+1) )

n = 3
for i in range(3): 
    print(" " * (n-i-1), end="")
    print("*" * (2*i+1), end="")
    print(" " * (n-i-1))
