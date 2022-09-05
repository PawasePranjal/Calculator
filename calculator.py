from calcs_utils import take_input, add_numbers, subtract_numbers, multiplication_numbers, division_numbers, \
    ask_operation

flag = -1
while flag == -1:
    flag, num_1, num_2 = take_input()


print(num_1, num_2)
ans = add_numbers(num_1, num_2)
print(f"the addition of two numbers is {ans}")
ans = subtract_numbers(num_1, num_2)
print(f" the subtraction of two numbers is {ans}")
ans = multiplication_numbers(num_1, num_2)
print(f"the multiplication of two numbers is {ans}")
ans = division_numbers(num_1, num_2)
print(f"the division of two numbers is {ans}")

flag = -1
while flag == -1:
    flag,op = ask_operation()


if op == 1:
    print("addition")
    ans = add_numbers(num_1, num_2)
    print(ans)


elif op == 2:
    print("subtraction")
    ans=subtract_numbers(num_1,num_2)
    print(ans)


elif op == 3:
    print("multiplication")
    ans=multiplication_numbers(num_1,num_2)
    print(ans)

elif op == 4:
    print("division")
    ans=division_numbers(num_1,num_2)
    print(ans)

