# def greet (name):
#     print("good evening" + name)


# greet("maani")


# def ans (num1,num2,num3):
#      return num1 + num2 + num3

# s = ans(1,2,3)
# print(s)


def maximum (num1,num2,num3):
   if(num1>num2):
    if(num1>num3):
        return num1
    else:
        return num2
   else:
    if(num2>num3):
        return num2
    else: 
        return num3

m = maximum(3,5,234)
print(m)   



