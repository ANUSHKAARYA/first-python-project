# sets list to empty listand target to user input 
list = []
target = int(input("Enter target: "))


def two_sum(list, target):
    for i in range(len(list)):
        for j in range(i+1, len(list)):
            if list[i] + list[j] == target:
                return [i, j] 


# Code to create a list of numbers from user input
while len(list) < 20:
    num = input("Enter a number: ")
    if num == "done":
        break
    else:
        list.append(int(num))

# Print the list of numbers
print(two_sum(list, target)) 

