
# 4
def check_parentheses(expr):
    s = []

    for i in range(len(expr)):

        if expr[i] == '(' or expr[i] == '[' or expr[i] == '{':
            s.append(expr[i])
            continue

        if len(s) == 0:
            return False

        if expr[i] == ')':

            x = s.pop()

            if x == '{' or x == '[':
                return False

        elif expr[i] == '}':

            x = s.pop()

            if x == '(' or x == '[':
                return False

        elif x == ']':

            x = s.pop()

            if x == '(' or x == '{':
                return False

    if len(s):
        return True
    else:
        return False


if __name__ == "__main__":

    expr = "{()}[]"

    if check_parentheses(expr):
        print("True")
    else:
        print("False")

# 5 Write a program to convert Integer to Roman String.

num_list = [(10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]


def num_roman(num):
    roman = ''

    while num > 0:
        for k, v in num_list:
            while num >= k:
                roman += v
                num -= k

    return roman


print(num_roman(105))

# 6
'''def count_code_lines(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1


print("Number of lines in the file: ", count_code_lines("E:\Python-classes\input code"))'''

# 7
import re


def check_password_strength(password):
    while True:
        if len(password) < 8:
            print("Week", ["The password must contain minimum 8 characters"])
            break
        elif not re.search("[a-z]", password):
            print("Week", ["The password must contain lower case alphabets"])
            break
        elif not re.search("[A-Z]", password):
            print("Week", ["The password must contain upper case alphabets"])
            break
        elif not re.search("[0-9]", password):
            print("Week", ["The password must contain a digit"])
            break
        elif not re.search("[!@#$&]", password):
            print("Week", ["The password must contain a special Character"])
            break
        else:
            return "Valid Password"


password = str(input("Enter the password: "))
print(check_password_strength(password))

# 8

def check_sentence(s):
    l = len(s)

    if s[0] < 'A' or s[0] > 'Z':
        return False

    if s[l - 1] != '.':
        return False

    prev_state = 0
    curr_state = 0

    index = 1

    while s[index]:

        if 'A' <= s[index] <= 'Z':
            curr_state = 0
        elif s[index] == ' ':
            curr_state = 1
        elif 'a' <= s[index] <= 'z':
            curr_state = 2
        elif s[index] == '.':
            curr_state = 3
        if prev_state == curr_state and curr_state != 2:
            return False
        if prev_state == 2 and curr_state == 0:
            return False
        if curr_state == 3 and prev_state != 1:
            return True

        index += 1

        prev_state = curr_state

    return False


s = str(input("Enter the string : "))
print(check_sentence(s))

# 9
def greatest_sub_array(arr,k, n):
    vec = []

    for i in range(n - k + 1):
        temp = []

        for j in range(i, i + k):
            temp.append(arr[j])

        vec.append(temp)

    vec = sorted(vec)

    return vec[len(vec) - 1]


arr = [1, 4, 3, 2, 5]
k = 4
n = len(arr)

ans = greatest_sub_array(arr, k, n)
print(list(ans))

# 10.Given a list of N integers. The task is to eliminate the minimum number of elements such that in the resulting
# list the sum of any two adjacent values is even.


def adj_sum_even(number):
    count = 0
    for num in range(len(number)):
        if number[num] % 2:
            count += 1
    return min(count, len(number) - count)


number = [1, 3, 5, 4, 2]
print(adj_sum_even(number))
