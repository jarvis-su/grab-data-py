print("hello ")
########################

def sumStartToEnd(start, end):
    sum = 0
    for n in range(start, end + 1, 1):
        sum = sum + n
    return sum


# if __name__ == '__main__' :
print(sumStartToEnd(1, 10000))

#######################################
def sum():
    sum = 0
    for n in range(1, 101):
        sum = sum + n
    return sum


print(sum())

##########################################
def sum():
    sum = 0
    x = 1
    while x < 101:
        sum = sum + x
        x += 1
    return sum


print(sum())

################################
def sum(x, y):
    return x + y


from functools import reduce

print(reduce(sum, range(1, 101)))
