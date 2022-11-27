# # 1.Countdown
def countdown(num):
    list = []
    for x in range(num, -1, -1):
        list.append(x)
    return list


# # 2. Print and Return
def print_and_return(x = []):
    if not x:
        print("please enter a list with a length of 2.")
    elif(len(x) > 2):
        print("please enter a list with a length of 2.")
    else:
        print(x[0])
        return(x[len(x)-1])


# # 3. First Plus Length
def first_plus_length(x = []):
    if not x:
        print("Please enter an array")
    else:
        sum = x[0] + x[len(x)-1]
        return sum

# # 4. Values Greater than Second
def values_greater_than_second(list):
    filteredList = []
    values = 0
    if(len(list) < 2):
        return False    
    for x in range(len(list)):
        if(list[x] > list[1]):
            filteredList.append(list[x])
            values += 1
    print(values)
    return filteredList

# y = values_greater_than_second([5,2,3,2,1,4])
# print(y)

# # 5. This Length, That Value
def length_and_value(length, value):
    list = []
    for x in range(length):
        list.append(value)
    
    return list


list1 = length_and_value(5, 7)

print(list1)