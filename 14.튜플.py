#list [] tuple()

numbers=(1,2,3,4)
number=1,2,3,4,
print(type(numbers))
print(type(number))

'''
number.append()#<< 사용불가
number.extends()#<< 사용불가
number.insert()#<< 사용불가
''' 

print(numbers+number)

print(numbers.index(3))
print(numbers[3])

number1=number[0]
number2=number[1]
number3=number[2]
number4=number[3]

number1,number2,*number3=number

print(number1,number2,number3)

numbers+=5,6,

print(numbers)
print(id(numbers))