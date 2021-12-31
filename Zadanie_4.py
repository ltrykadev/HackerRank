import re

if __name__ == '__main__':
    count = int(input())

x = 0
number_list = []

while x < count:
    number_input = input()
    number_list.append(number_input)
    x += 1

for number in number_list:
    if len(number) == 10:
        match_first = re.search(r'^[789]', number)
        if match_first:
            match_second = re.search(r'[^0-9]', number)
            if match_second:
                print("NO")
            else:
                print("YES")
        else:
            print("NO")
    else:
        print("No")