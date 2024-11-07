
dict1 ={
    'value':11
}
dict2 = dict1

print("Before num2 value is updated :")
print("num1 = ",dict1)
print("num2 = ",dict2)

print("\nnum1 points to : ", id(dict1))
print("num2 points to :",id(dict2))

dict2['value'] = 22

print("\nNow num2 value is updated :")
print("num1 = ",dict1)
print("num2 = ",dict2)

print("\nnum1 points to : ", id(dict1))
print("num2 points to :",id(dict2))